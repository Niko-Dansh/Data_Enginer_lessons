# extract_points_labels_fixed.py

import csv
import time
from math import sqrt
from pyautocad import Autocad, APoint

def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def main(dwg_path, csv_path, tol=5.0):
    # 1) Подключаемся (если нет — запустим новый экземпляр AutoCAD)
    acad = Autocad(create_if_not_exists=True)
    # 2) Ждём пару секунд, чтобы COM-объект успел инициализироваться
    time.sleep(2)

    # 3) Открываем документ
    doc = acad.app.Documents.Open(dwg_path)
    ms  = doc.ModelSpace

    # 4) Собираем все однострочные тексты (Text, MText)
    texts = []
    for ent in ms:
        name = getattr(ent, 'ObjectName', '')
        if name in ('AcDbText', 'AcDbMText'):
            ins_pt = APoint(ent.InsertionPoint)
            txt    = ent.TextString.strip()
            texts.append((ins_pt, txt))

    # 5) Перебираем все точки и сопоставляем ближайший текст
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(('X','Y','Z','Label'))
        for ent in ms:
            if getattr(ent, 'ObjectName', '') == 'AcDbPoint':
                p = APoint(ent.Coordinates)
                best_d, best_txt = tol, ''
                for t_pt, t_txt in texts:
                    d = distance(p, t_pt)
                    if d < best_d:
                        best_d, best_txt = d, t_txt
                writer.writerow((p.x, p.y, p.z, best_txt))

    # 6) Закрываем документ и сам AutoCAD (если нужно)
    doc.Close(False)
    acad.app.Quit()
    print(f'Готово, записи в {csv_path}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print('Usage: python extract_points_labels_fixed.py <dwg> <csv> [tolerance]')
        sys.exit(1)
    dwg     = sys.argv[1]
    csv_out = sys.argv[2]
    tol     = float(sys.argv[3]) if len(sys.argv) > 3 else 5.0
    main(dwg, csv_out, tol)


#python extract_points_labels_fixed.py "C:\Users\naunn\PycharmProjects\Data_Enginer_lessons\1 этаж выгрузка.dwg" "C:\Users\naunn\PycharmProjects\Data_Enginer_lessons\output.csv" 0.05
