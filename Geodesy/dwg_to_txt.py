# -*- coding: utf-8 -*-
import math
import time
from comtypes import COMError
from pyautocad import Autocad, APoint

def fmt_txt(val):
    """Для points.txt: 4 знака после запятой, десятичный – запятая"""
    return f"{val:.4f}".replace('.', ',')

def fmt_f(val, prec=3):
    """Быстрое форматирование float с точкой и заданной точностью"""
    return f"{val:.{prec}f}"

def pad_left(s, width):
    """Правильное выравнивание по правому краю в поле ширины width"""
    s = str(s)
    return ' ' * max(0, width - len(s)) + s

def pad_right(s, width):
    """Правильное выравнивание по левому краю в поле ширины width"""
    s = str(s)
    return s + ' ' * max(0, width - len(s))

def iter_modelspace(acad):
    """Надежно итерируем по ModelSpace, с ретраями на COMError"""
    for attempt in range(5):
        try:
            ms = acad.doc.ModelSpace
            for e in ms:
                yield e
            return
        except COMError:
            time.sleep(0.3)
    raise RuntimeError("Не удалось получить доступ к ModelSpace")

def main():
    acad = Autocad(create_if_not_exists=False)

    # 1) Собираем все тексты из ModelSpace
    texts = []
    for e in iter_modelspace(acad):
        on = e.ObjectName
        if on == 'AcDbText':
            texts.append({
                'content': e.TextString,
                'pos': (e.InsertionPoint[0], e.InsertionPoint[1])
            })
        elif on == 'AcDbMText':
            texts.append({
                'content': e.Contents,
                'pos': (e.InsertionPoint[0], e.InsertionPoint[1])
            })

    records = []  # сюда пойдёт (label, y, x, z)

    # 2) Проходим по точкам и собираем в points.txt + в records
    with open('points.txt', 'w', encoding='utf-8') as f_txt:
        for e in iter_modelspace(acad):
            if e.ObjectName != 'AcDbPoint':
                continue
            pt = APoint(e.Coordinates)
            # собираем подписи в радиусе 3.0
            nearby = []
            for txt in texts:
                dx = pt.x - txt['pos'][0]
                dy = pt.y - txt['pos'][1]
                if math.hypot(dx, dy) <= 3.0:
                    nearby.append(txt)
            if not nearby:
                print(f"Point @({fmt_txt(pt.x)},{fmt_txt(pt.y)}) — нет подписей, skip")
                continue

            nearby.sort(key=lambda t: math.hypot(pt.x - t['pos'][0],
                                                pt.y - t['pos'][1]))
            cand = nearby[:2]
            # выбираем ту, что выше по Y
            if len(cand) == 1:
                top = cand[0]
                name = top['content'].strip()
            else:
                a, b = cand
                top, bot = (a, b) if a['pos'][1] >= b['pos'][1] else (b, a)
                name = top['content'].strip()

            y, x, z = pt.y, pt.x, pt.z
            line_txt = f"{name}\t{fmt_txt(y)}\t{fmt_txt(x)}\t{fmt_txt(z)}\n"
            f_txt.write(line_txt)
            records.append((name, y, x, z))
            print("TXT:", line_txt.strip())

    # 3) Генерируем points_6k.sdr
    header = [
        "00NMSDR33 V04-04.02     06-ЁЮН-25 14:01 111111",
        "10NMREI2            121111",
        "06NM1.00000000      ",
        "01NM:ES-105 V02-57   HP1060ES-105 V02-57   HP106031                                0.000           ",
        "03NM0.000           "
    ]
    with open('points_6k.sdr', 'w', encoding='utf-8') as f_sdr:
        # пишем шапку
        for h in header:
            f_sdr.write(h.rstrip() + "\n")

        # для каждой записи собираем 5 полей по 16 символов
        for name, y, x, z in records:
            seg1 = pad_left(name, 16)     # название, right-aligned
            seg2 = pad_right(fmt_f(y,3),  16)  # Y, left-aligned
            seg3 = pad_right(fmt_f(x,3),  16)  # X
            seg4 = pad_right(fmt_f(z,3),  16)  # Z
            seg5 = pad_right("IS",        16)  # кодировка точек

            line_sdr = "08TP" + seg1 + seg2 + seg3 + seg4 + seg5
            f_sdr.write(line_sdr.rstrip() + "\n")
            print("SDR:", line_sdr)

    print("\nГотово! Сгенерированы:\n - points.txt\n - points_6k.sdr")

if __name__ == "__main__":
    main()