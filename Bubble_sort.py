# 8. Прочитать в интернете, что такое сортировка пузырьком.
# Написать себе на листке алгоритм, после чего написать функцию, которая на вход получает список (list), сортирует его пузырьком, после чего возвращает отсортированный список.
# Про сортировку пузырьком теория:
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC

list_unsorted = [2,1,3,4]
# print(list_unsorted,'start')

list_lenght = len(list_unsorted)
# for number in range(n - 1):
#     if list_unsorted[number] > list_unsorted[number + 1]:
#         list_unsorted[number], list_unsorted[number + 1] = list_unsorted[number + 1], list_unsorted[number]
#         print(list_unsorted)
#
# print(list_unsorted,'end')


# for number in range(list_lenght - 1):
#     if list_unsorted[number] < list_unsorted[number + 1]:
#         continue
#
#     else:
# #         list_unsorted[number], list_unsorted[number + 1] = list_unsorted[number + 1], list_unsorted[number]
# #         print(f'{number} pair is NOT ok')
#
#
# #Я задолбался вот решение от чатгпт, но и его пришлось исправлять до оптимальности, зато я запомнил класную идею с флагом, которая предотвращает лишние итерации.
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):# Проходим по массиву n-1 раз
#         swapped_once = False # Создадим флаг для проверки на сортированность, чтобы лишние циклы не делать
#         for j in range(0, n - i - 1):# На каждой итерации "всплывает" наибольший элемент
#             if arr[j] > arr[j + 1]:# Если текущий элемент больше следующего, меняем их местами
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped_once = True # Фиксируем факт 1 перестановки, флажок щелкнулся
#         if not swapped_once:
#             print('not swaped once')
#             break
#     return arr
#
# # Пример использования
# array = [2, 1, 3, 8, 5, 6, 9]
# sorted_array = bubble_sort(array)
# print("Отсортированный массив:", sorted_array)
#

def my_bubble_sort(list_): # Принимаем список, должно работать и с int и float
    n_cycles = len(list_) # Просто количество циклов n
    for i in range(n_cycles - 1): # Проходим цикл n-1 раз, где n - длинна списка, пар получается на 1 меньше
        swapped_once = False # Ставим флажок, который будет отражать была ли илил небыло перестановки в положение False, и какждый раз в цикле переставляем, что перестановки не было на этом кругу цикла, если в дальнейшем престановок и не будет, то список отсортирован
        for j in range(n_cycles - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                swapped_once = True
            if not swapped_once:
                break
    return list_
























def my_bubble_sort_2(list_):
    n_cylels = len(list_)
    for i in range(n_cylels - 1):
        swapped_once = False
        for j in range(n_cylels - 1 - i):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]
                swapped_once = True
        if not swapped_once:
            break
    return list_


array = [2, 1, 3, 8, 5, 6, 9]
sorted_array = my_bubble_sort_2(array)
print("Отсортированный массив 2:", sorted_array)
