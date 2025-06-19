# extract_points_labels.py

import csv
from math import sqrt
from pyautocad import Autocad, APoint

def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

def main(dwg_path, csv_path, tol=5.0):
    """
    dwg_path  - путь к вашему DWG-файлу
    csv_path  - путь к выходному CSV
    tol       - радиус поиска подписи рядом (в единицах чертежа)
    """
    acad = Autocad(create_if_not_exists=False)
    acad.prompt("Открываю чертеж…\n")
    acad.doc = acad.app.Documents.Open(dwg_path)
    ms = acad.doc.ModelSpace

    # Собираем все тексты в список (однострочные Text и MText)
    texts = []
    for txt in ms:
        if txt.ObjectName in ("AcDbText", "AcDbMText"):
            # Для MText используем .TextString, для Text — .TextString
            texts.append((APoint(txt.InsertionPoint), txt.TextString.strip()))

    # Открываем CSV на запись
    with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(("Point_X", "Point_Y", "Point_Z", "Label"))
        # Перебираем все точки
        for pt in ms:
            if pt.ObjectName == "AcDbPoint":
                p = APoint(pt.Coordinates)
                # ищем самый близкий текст в пределах tol
                best = None
                best_d = tol
                for (tpt, txt) in texts:
                    d = distance(p, tpt)
                    if d < best_d:
                        best_d = d
                        best = txt
                label = best if best else ""
                writer.writerow((p.x, p.y, p.z, label))

    acad.doc.Close(False)
    acad.app.Quit()
    print(f"Готово! Выгрузили в {csv_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python extract_points_labels.py <path_to_dwg> <path_to_csv> [tolerance]")
        sys.exit(1)
    dwg, csvf = sys.argv[1], sys.argv[2]
    tol = float(sys.argv[3]) if len(sys.argv) >= 4 else 5.0
    main(dwg, csvf, tol)


