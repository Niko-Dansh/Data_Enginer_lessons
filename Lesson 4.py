# 1. Написать цикл по листу.
work_list = [1, 2.3, 4, 5, 6, 7]
chat_gpt_list = [10, 20, 30, 40, 50]

work_list = list(set(work_list))
for element in work_list:
    print(f'Индекс {element} в списке work_list = {work_list.index(element)}')

for element in chat_gpt_list:
    print(f'ChatGPT создал список с элемтом {element} под индексом {chat_gpt_list.index(element)}')

print(work_list + chat_gpt_list)
for index, item in enumerate(work_list + chat_gpt_list):
    print(f'Индекс {item} в объединенном списке work_list + chat_gpt_list = {index}')

#2. Написать цикл по листу со строками. Выводить значения, если длина строки элемента > 5 символов.

work_list2 = ['eniki', 'beniki', 'eli', 'vareniki', 'lol', 'kek', 'cheburek']

for element in work_list2:
    if len(element) > 5:
        print(element)

# 3. Написать цикл по листу с листами. Внутри цикла по внешнему листу - сделать цикл по внутренним листикам. Просто выводить элементы.

list_with_lists = [
    [1, 2, 3],
    ['a', 'b', 'c'],
    [True, False],
    ['Python', 'is', 'fun'],
]

for element in list_with_lists:
    for element_2 in element:
        print(element_2)

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f'Индекс {index}: фрукт {fruit}')



# 4. Написать цикл по словарю (по ключам словаря). Выводить ключи и выводить значения.

from Дела_работа import список_дел

print(список_дел)
print(list(список_дел.keys()))

collect_work_items_dict = список_дел.get('Собрать одежду и оборудование по геодезии на первае время') | список_дел.get('Собрать кухонные принадлежности')

print(collect_work_items_dict)

for item_key,item_value in collect_work_items_dict.items():
    print(item_key,item_value)

# 5. Вывести цифры от 1 до 10000 используя цикл while и break. Про continue я всё неправильно рассказал - continue лучше не используйте.

item = 0
while item < 100:
    item += 1
    print(item)

item = 0
while True:
    item += 1
    print(item)
    if item >= 100:
        break


# 6. Создайте 2 словаря с различными ключами. Сделайте 3й словарь - чтобы там были значения и из 1го словаря и из второго - используя цикл по второму словарю.

work_dict_6_1, work_dict_6_2 = список_дел.get('Собрать одежду и оборудование по геодезии на первае время'), список_дел.get('Собрать кухонные принадлежности')

print(work_dict_6_1.keys(), work_dict_6_2.keys())

work_dict_6_1_and_2_merged = work_dict_6_1
for item_key, item_value in work_dict_6_2.items():
    work_dict_6_1[item_key] = item_value

print('work_dict_6_1_and_2_merged =', work_dict_6_1_and_2_merged)


