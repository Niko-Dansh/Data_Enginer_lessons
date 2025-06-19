my_list = [1, 2, 3, 2]
my_tuple = (1, 2, 3, 2)
my_set = {1, 2, 3, 2}  # результат: {1, 2, 3}
my_dict = {'name': 'Alice', 'age': 30, 'age': 25}  # 'age' будет 25

# print(my_list)
# print(my_tuple)
# print(my_set)
# print(my_dict)
my_list.append('privet')

# print(my_list.append('privet'))
#print(my_tuple.append('privet'))
#print(my_set.append('privet'))
#print(my_dict.append('kek': 'privet'))

for var_key, var_value in locals().copy().items():
    if var_key.startswith('my_'):
        print(f'{var_key}: {var_value}')
