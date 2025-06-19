# filename: clean_dwg.py

import time
from pyautocad import Autocad
import comtypes

def iterate_space(space, space_name=""):
    """
    Итератор по объектам в пространстве (ModelSpace или BTR).
    Проходит по индексам с конца к началу, чтобы можно было удалять на лету.
    """
    try:
        count = int(space.Count)
    except Exception as e:
        print(f"[{space_name}] Не удалось получить Count: {e}")
        return

    # проходим в обратном порядке
    for i in range(count - 1, -1, -1):
        try:
            obj = space.Item(i)
            yield obj
        except comtypes.COMError as e:
            # пропускаем «отклонённые» вызовы
            print(f"[{space_name}] COMError при доступе к Item({i}): {e}")
        except Exception as e:
            print(f"[{space_name}] Ошибка при доступе к Item({i}): {e}")

def explode_space_blocks(space, space_name=""):
    """
    Взрывает все BlockReference в указанном пространстве.
    """
    exploded = 0
    for obj in iterate_space(space, space_name):
        if obj.ObjectName == "AcDbBlockReference":
            try:
                obj.Explode()
                obj.Delete()
                exploded += 1
            except Exception as e:
                print(f"[{space_name}] Ошибка Explode/Delete: {e}")
    if exploded:
        print(f"[{space_name}] Взорвано и удалено {exploded} BlockReference.")

def delete_non_poly(space, keep_types, space_name=""):
    """
    Удаляет из пространства всё, кроме объектов с типами в keep_types.
    """
    deleted = 0
    for obj in iterate_space(space, space_name):
        if obj.ObjectName not in keep_types:
            try:
                obj.Delete()
                deleted += 1
            except Exception as e:
                print(f"[{space_name}] Не удалось удалить {obj.ObjectName}: {e}")
    if deleted:
        print(f"[{space_name}] Удалено {deleted} объектов (не полилинии/линии).")

def main():
    acad = Autocad(create_if_not_exists=False)
    doc = acad.doc
    print(f"Connected to AutoCAD. Документ: {doc.Name}")

    # 1) Explode в ModelSpace
    explode_space_blocks(doc.ModelSpace, "ModelSpace")

    # 2) Explode на каждом Layout (PaperSpace)
    for layout in doc.Layouts:
        if not layout.ModelType:  # если не Model, т.е. лист
            btr = layout.Block
            explode_space_blocks(btr, f"Layout «{layout.Name}»")

    # 3) Удаляем всё, что не Line или Polyline
    KEEP_TYPES = {"AcDbLine", "AcDbLWPolyline", "AcDbPolyline"}
    delete_non_poly(doc.ModelSpace, KEEP_TYPES, "ModelSpace")
    for layout in doc.Layouts:
        if not layout.ModelType:
            delete_non_poly(layout.Block, KEEP_TYPES, f"Layout «{layout.Name}»")

    # 4) Пора запускать очистку AutoCAD
    time.sleep(0.5)
    doc.SendCommand('с * _Y \n')
    time.sleep(0.3)
    doc.SendCommand('_.OVERKILL _ALL \n\n')
    time.sleep(0.3)
    doc.SendCommand('_.REGENALL \n')

    print("Готово! Не забудьте сохранить файл под новым именем.")

if __name__ == "__main__":
    main()