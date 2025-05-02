a = []
b = a
print(a is b)  # True, так как a и b ссылаются на один и тот же объект
print(a == b)


# Домашнее задание:
# 1. Написать функцию без параметров.

def simple_function():
    return 'Это функция без параметра))'

print(simple_function())


# 2. Написать функцию с 1 параметром.

def one_param_func(parametr):
    return f'{parametr} - вот такой парпаметр в этой функции'

print(one_param_func(None))

# 3. Написать функцию с 3 параметрами.

def three_parametr_function(first, second, third):
    return f'{first}, {second}, {third} - вот 3 параметра у этой функции,с ними можно что-то делать!!!'

print(three_parametr_function(1,2,3))

# 4. Написать функцию с 3 параметрами - и последнему параметру задать значение по умолчанию.

def funk_with_3_param_3rd_default(pervi, vtoroi, tretiy=3):
    return f'{pervi}, {vtoroi}, {tretiy} - вот тут 3 параметра, 3й должен быть по умолчанию'

print(funk_with_3_param_3rd_default(pervi=1,vtoroi=2))

# 5. Функцию с 1 параметром вызвать внутри цикла.

i = 0
while True:
    i += 1
    print(simple_function(),':',i)
    if i >= 12:
        break


# 6. Написать функцию с 1 параметром - и в этот параметр передать переменную типа list.
# Функция должна возвращать сумму всех элементов list, который в неё передали.
# Возвращать через return - а не просто через print выводить.


def sum_of_the_list(list_1):
    sum_1 = 0
    for item in list_1:
        sum_1 = sum_1 + item

    return sum_1


print(sum_of_the_list([1,2,3,4]))

# 7. Вызвать одну функцию внутри другой.

def func_in_func(list_2):
    return {
        'Список': list_2,
        'Сумма элементов списка':sum_of_the_list(list_2),
    }

print(func_in_func([1,2,3]))
print(f'У нас есть список {func_in_func([1,2,3]).get('Список')} сумма элементов которого равна {func_in_func([1,2,3]).get('Сумма элементов списка')}')

# 8. Прочитать в интернете, что такое сортировка пузырьком. Написать себе на листке алгоритм, после чего написать функцию, которая на вход получает список (list), сортирует его пузырьком, после чего возвращает отсортированный список.
# Про сортировку пузырьком теория:
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%BF%D1%83%D0%B7%D1%8B%D1%80%D1%8C%D0%BA%D0%BE%D0%BC

from  Bubble_sort import my_bubble_sort

# Пример использования
array = [2, 1, 3, 8, 5, 6, 9]
sorted_array = my_bubble_sort(array)
print("Отсортированный массив:", sorted_array)