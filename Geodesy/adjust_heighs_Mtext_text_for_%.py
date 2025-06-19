# -*- coding: utf-8 -*-
"""
adjust_heights.py

Автокад+pyautocad: находит все MText (AcDbMText) и однострочные Text (AcDbText),
на всякий случай пробует три варианта геттера/сеттера текста,
умножает все найденные числа на (1 + percent/100) и округляет до 2 знаков.
"""

import re
import comtypes
from pyautocad import Autocad

def main():
    percent = -4.25945
    factor = 1 + percent/100.0

    # Компиляция регулярки один раз
    num_re = re.compile(r'-?\d+(?:\.\d+)?')

    acad = Autocad(create_if_not_exists=False)
    acad.prompt(f"Начинаю корректировать глубины на {percent}% …\n")

    updated = 0

    for ent in acad.doc.ModelSpace:
        obj = ent.ObjectName  # например, 'AcDbMText' или 'AcDbText'

        # обрабатываем только чистые MText и Text
        if obj == 'AcDbMText':
            # у MText бывают разные интерфейсы: Contents, Text или TextString
            orig = None
            for prop in ('Contents', 'Text', 'TextString'):
                try:
                    orig = getattr(ent, prop)
                    write_prop = prop
                    break
                except (NameError, AttributeError, comtypes.COMError):
                    continue
            if orig is None:
                # не нашли подходящего свойства — пропускаем
                continue
            setter = lambda s, p=write_prop: setattr(ent, p, s)

        elif obj == 'AcDbText':
            # у однострочных Text’ов всегда TextString
            try:
                orig = ent.TextString
            except (NameError, AttributeError, comtypes.COMError):
                continue
            setter = lambda s: setattr(ent, 'TextString', s)

        else:
            continue

        # подстановка: каждое вхождение числа
        def repl(m):
            val = float(m.group(0))
            return f"{val * factor:.2f}"

        new = num_re.sub(repl, orig)

        if new != orig:
            setter(new)
            updated += 1
            acad.prompt(f"  → {obj}: «{orig}» → «{new}»\n")

    acad.prompt(f"Готово. Обновлено объектов: {updated}\n")


if __name__ == '__main__':
    main()