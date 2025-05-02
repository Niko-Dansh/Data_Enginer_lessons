from Lesson2 import list1

# print(list1[0])

d1 = {1:1, 2:2}
d2 = dict(one=1, two=2)
d1['first'] = '1st'
d1['last'] = 'lust'
d2[3] = 'thitst'
d3 = {
    '1st': d1,
    '2nd': d2,
    '3rd': list1,
}
d4 = d1 | d2
d5 = { **d1, **d2}
d6 = {
    'd1': {1:1, 2:2},
    'd2': d2,
}
d6_get_get = d6.get('d1').get(1)
d6_get_get_2 = d6.get('d2').get('two')
d6['d3'] = {3:3, 4:4}

d1_keys_list = list(d1.keys())
d1_values_list = list(d1.values())

d1.update(d2)

# print(d1)
# print(d2)
# print(d3)
# print(d4)
# print(d1)
# print(d5)
#
# print('locals= ', locals())
# print('d1= ', d1)
# print('d2= ', d2)
# print('d3= ', d3)
# print('d4= ', d4)
# print('d1= ', d1)
# print('d5= ', d5)

# for var_name, var_value in locals().copy().items():
#     if var_name.startswith('d'):
#         print(f'{var_name} = {var_value}')
# # print('\n')

# # Вывод всех переменных с их именами
# for var_name, var_value in locals().items():
#     if var_name.startswith('d'):  # Фильтруем только переменные, начинающиеся на 'd'
#         print(f'{var_name}= {var_value}')

d5_keys_list =list(d5.keys())
d5_keys_tuple =tuple(d5.keys())
d5_keys_set = set(d5.keys())

d5_values_list = (list(d5.values()))[0:3]
d5_values_set = set(d5.values())

# for var_name, var_value in locals().copy().items():
#     if var_name.startswith('d5_'):
#         print(f'{var_name} = {var_value}')
# # print('\n')


d5_get_1 = d5.get(1)
d5_get_2 = d5.get(2)
d5_get_first = d5.get('first')
d5_get_first_2 = d5['first']
d5_gitems = set(d5.items())

for var_name, var_value in locals().copy().items():
    if var_name.startswith('d'):
        print(f'{var_name} = {var_value}')
# print('\n')