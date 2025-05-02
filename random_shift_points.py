# random_shift_points.py
from pyautocad import Autocad, APoint
import random

def main(mm=3.0):
    acad = Autocad(create_if_not_exists=False)
    for pt in acad.iter_objects('AcDbPoint'):  # или 'Point'
        if pt.Layer == '2':
            x, y, z = pt.Coordinates
            # случайный сдвиг в диапазоне [-mm, +mm]
            dx = random.uniform(-mm, mm)
            dy = random.uniform(-mm, mm)
            dz = random.uniform(-mm, mm)
            # удаляем старую точку и создаём новую
            pt.Delete()
            acad.model.AddPoint(APoint(x + dx, y + dy, z + dz))
    print("Готово: все точки смещены.")

if __name__ == "__main__":
    main(0.003)