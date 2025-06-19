#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
split_CSV_with_header.py

Тот же split_CSV.py, но с сохранением первых N заголовочных строк во все файлы.
Использование:
    python split_CSV_with_header.py Koord.CSV ST1 ST2 ST3
Результат:
    ST1.CSV, ST2.CSV, ST3.CSV с первыми 4 строками + только свои станции.
"""

import sys
import os

# Сколько заголовочных строк копировать в начало каждого файла
N_HEADER = 0

def split_by_stations(input_path, stations, n_header=N_HEADER):
    if not os.path.isfile(input_path):
        print(f"Ошибка: файл «{input_path}» не найден.")
        sys.exit(1)

    # Читаем всё в бинарном виде, чтобы сохранить кодировку и любые невидимые байты
    with open(input_path, 'rb') as f:
        lines = f.readlines()

    # Разделяем на заголовок и рабочие данные
    header = lines[:n_header]
    body   = lines[n_header:]

    for station in stations:
        keyword = station.encode('ascii', errors='ignore')
        out_name = f"{station}.CSV"
        with open(out_name, 'wb') as out:
            # Сначала пишем заголовок
            for h in header:
                out.write(h)
            # Затем фильтруем по ключевому слову
            for line in body:
                if keyword in line:
                    out.write(line)
        print(f"Создан файл «{out_name}»: {n_header} строк заголовка + строки с «{station}».")

def main():
    if len(sys.argv) < 3:
        print("Использование: python split_sdr_with_header.py Koord.CSV ST1 ST2 ST3 ...")
        sys.exit(1)

    input_file = sys.argv[1]
    stations   = sys.argv[2:]
    split_by_stations(input_file, stations)

if __name__ == "__main__":
    main()