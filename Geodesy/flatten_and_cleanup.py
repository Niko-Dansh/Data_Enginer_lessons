# filename: flatten_and_cleanup_v2.py

import os
import time
from pyautocad import Autocad
import comtypes
from comtypes import COMError

# Код формата R12 DXF в AutoCAD COM API
ACAD_SAVEAS_R12_DXF = 16

def delete_non_poly(doc, keep_types):
    """
    Удаляем из ModelSpace всё, кроме тех типов, что указаны в keep_types.
    """
    ms = doc.ModelSpace
    try:
        cnt = int(ms.Count)
    except Exception:
        return
    # идём с конца к началу, чтобы удалять «на лету»
    for i in range(cnt - 1, -1, -1):
        try:
            obj = ms.Item(i)
            if obj.ObjectName not in keep_types:
                obj.Delete()
        except Exception:
            pass

def main():
    acad = Autocad(create_if_not_exists=False)
    src_doc = acad.doc
    src_path = src_doc.FullName
    src_folder = os.path.dirname(src_path)
    base_name = os.path.splitext(os.path.basename(src_path))[0]

    # 1) Экспорт в R12 DXF без диалогов
    out_dxf = os.path.join(src_folder, base_name + "_flat.dxf")
    if os.path.exists(out_dxf):
        os.remove(out_dxf)
    print(f"1) Saving as R12 DXF → {out_dxf}")
    try:
        # параметры: (имя_файла, формат)
        src_doc.SaveAs(out_dxf, ACAD_SAVEAS_R12_DXF)
    except COMError as e:
        print("Ошибка SaveAs DXF:", e)
        return

    # Небольшая задержка на диск
    time.sleep(1)
    if not os.path.exists(out_dxf):
        print("DXF не появился на диске, что-то пошло не так.")
        return

    # 2) Открываем DXF как новый документ
    print("2) Opening DXF...")
    try:
        flat_doc = acad.app.Documents.Open(out_dxf)
    except COMError as e:
        print("Не удалось открыть DXF:", e)
        return

    # 3) Удаляем из него всё, кроме полилиний/линий
    print("3) Deleting everything except lines and polylines...")
    KEEP = {"AcDbLine", "AcDbLWPolyline", "AcDbPolyline"}
    delete_non_poly(flat_doc, KEEP)

    # 4) Чистим служебщину и дубликаты
    print("4) Running PURGE / OVERKILL / REGENALL...")
    time.sleep(0.2)
    flat_doc.SendCommand('_.-PURGE _ALL * _Y \n')
    time.sleep(0.2)
    flat_doc.SendCommand('_.OVERKILL _ALL \n\n')
    time.sleep(0.2)
    flat_doc.SendCommand('_.REGENALL \n')
    time.sleep(0.5)

    # 5) Сохраняем в новый DWG
    out_dwg = os.path.join(src_folder, base_name + "_flat_clean.dwg")
    if os.path.exists(out_dwg):
        os.remove(out_dwg)
    print(f"5) Saving final DWG → {out_dwg}")
    try:
        # формат 0 = текущий формат DWG
        flat_doc.SaveAs(out_dwg, 0)
    except COMError as e:
        print("Ошибка SaveAs DWG:", e)
        return

    print("Done! Лёгкий чертеж:", out_dwg)

    # (по желанию) закрываем временный DXF-документ
    # flat_doc.Close(False)

if __name__ == "__main__":
    main()