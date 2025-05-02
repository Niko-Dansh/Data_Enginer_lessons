# random_shift_points_move.py
from pyautocad import Autocad, APoint
import random


def rand_shift_points(layer='0', mm=3.0):
    acad = Autocad(create_if_not_exists=False)
    shift = mm / 1000.0  # из мм в единицы чертежа

    base = APoint(0, 0, 0)
    count = 0
    for ent in acad.iter_objects():  # перебираем ВСЕ объекты
        # проверяем, что это точка AutoCAD и нужный слой
        if hasattr(ent, 'ObjectName') and ent.ObjectName in ('AcDbPoint',) and ent.Layer == layer:
            dx = random.uniform(-shift, shift)
            dy = random.uniform(-shift, shift)
            dz = random.uniform(-shift, shift)
            vec = APoint(dx, dy, dz)
            ent.Move(base, vec)
            count += 1

    print(f"Готово: сдвинуто {count} точек в слое \"{layer}\" на ±{mm} мм.")


if __name__ == '__main__':
    import sys

    # можно передать слой и смещение из командной строки
    layer = sys.argv[1] if len(sys.argv) > 1 else '0'
    mm = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
    rand_shift_points(layer, mm)