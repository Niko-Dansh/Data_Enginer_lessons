# list_1 = ['apple', 'orange']
# list_2 = ['banana', 'watermelon']
#
# list_result_1 = list_1 + list_2
#
# print(list_result_1)
#
# list_1.append(list_2)
#
# print(list_1)
#
# list_1.remove(list_2)
#
# print(list_1)
#
# list_1.extend(list_2)
#
# print(list_1)
#
# list_1.pop(2)
# list_1.pop(2)
#
# print(list_1)
#
# for item in list_2:
#     list_1.append(item)
#
# print(list_1)
#
# dict_1 = {
#     'key_1': 1,
#     'key_2': 2,
#     'key_3': 3
# }
#
# print(dict_1.get('key_4'))
#
# print(dict_1.keys())
# print(dict_1.values())
#
# list_of_keys = list(dict_1.keys())
# list_of_values = list(dict_1.values())
#
# dict_result = {}
# for key, value in list_of_keys, list_of_values:
#     dict_result[key] = value
#
#
# print(dict_result)
#
#
# for item in list_1:
#     if len(item) > 5:
#         print(item)
#
#
# for inner_list in outer_list:
#     for item in inner_list:
#         print item


# i = 0
# while i < 1000:
#     i += 1
#     print(i)

# def inner_function():
#     return 3.149
#
# def outer_function():
#     return inner_function()*2
#
# print(outer_function())
#
#
# def list_sum(lst):
#     v_summ = 0
#     for item in lst:
#         v_summ += item
#     return v_summ
#
# list_3 = [1, 2, 3]
#
# print(list_sum(list_3))
#
#
# list_4 = [1, 2, 3, 4, 5, 6]
#
# def bubble_sort(lst):
#     n = len(lst) - 1 # количество циклов на 1 меньше длинны
#     sorted_list = []
#     for i in range(n): # необязательно проходить по всем циклам, если все элементы отсортированы за один проход
#         for item in lst:
#             if item > lst[i]:
#                 lst[i - 1] = lst[i]
#                 lst[i] = item
#     return lst
#
#
# print(bubble_sort(list_4))
#
#
# class MyError(ValueError):


# import datetime
#
# current_time = datetime.datetime.now()
#
# one_hour = datetime.timedelta(hours=1)
#
# time_minus_one_hour = current_time - one_hour
# print(time_minus_one_hour)
#
# pip istall pandas

import pandas as pd

# list_5 = [{1},{2},{3}]
# my_dataframe = list_5.pd.df
object
NotImplemented


