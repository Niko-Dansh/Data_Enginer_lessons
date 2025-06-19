from traceback import print_tb
import random
import string

a = -1
b = 0
c = 1

#1. Использовать условный оператор - сравнить несколько чисел и вывести что-нибудь в print
if a > b:
    print(f'a(={a}) > b(={b})')
else:
    print('Nope')

if b == (c - 1):
    print('b = (c - 1)')

else:
    'Nope'

a += -1
b -= 0
c = 1

if a > b:
    print(f'a(={a}) > b(={b})')
else:
    print('Nope')

if b == (c - 1):
    print('b = (c - 1)')

else:
    'Nope'

if True:
    print(True)
else:
    print(False)

a = int((random.uniform(-10,10)))
b -= 0
c = 1

print(a)

if (a > b) and (a > c):
    print('a > b, a > c')
else:
    print('Suck my balls')

#2. Использовать условный оператор - и если число в переменной положительное - умножить его на 10,
# а если отрицательное - разделить.

x = int((random.uniform(-10,10)))

print('x random = ',x)

if x == 0:
    print(F'x = {x}, nothing can be done')
elif x > 0:
    x = 10*x
else:
    x = x/10

print(f'x now equals {x}')

#3. Если число кратно 2м - то разделить его на 2 и вывести - иначе - умножить на 3.
# Как детектировать кратность числа в питоне - погуглите.

x3 = int((random.uniform(-10,10)))

print('x3 = ', x3)

print('x3 % 2 = ', x3 % 2)
if (x3 % 2 == 0):
    x3 = x3/2
    print('x3(четное) = ', x3)
else:
    x3 = x3 * 3
    print('x3(нечетное) = ', x3)

#4. Сделать какой-нибудь if внутри if.

# names = ["Анна", "Максим", "София", "Александр", "Полина", "Иван", "Екатерина", "Михаил", "Дарья", "Артём"]
# names = list(set(names))
# print('names = ', names)

names_with_gender = [
    {"name": "Анна", "gender": "female"},
    {"name": "Максим", "gender": "male"},
    {"name": "София", "gender": "female"},
    {"name": "Александр", "gender": "male"},
    {"name": "Полина", "gender": "female"},
    {"name": "Иван", "gender": "male"},
    {"name": "Екатерина", "gender": "female"},
    {"name": "Михаил", "gender": "male"},
    {"name": "Дарья", "gender": "female"},
    {"name": "Артём", "gender": "male"},
    {"name": "Гнвоерк", "gender": "(O@#Y(@H"}
]

names_dict = {}
for single_name in names_with_gender:
    names_dict[single_name["name"]] = single_name["gender"]
print('names_dict = ',names_dict)

i = 0
names_dict_with_get = {}
for single_name in names_with_gender:
    names_dict_with_get[single_name.get("name")] = single_name.get("gender")
    print(f'names_dict_with_get_{i} = ',names_dict_with_get)
    i += 1
print(f'names_dict_with_get_end_{i} = ',names_dict_with_get)


random_name = random.choice(list(names_dict.keys()))
print('random_name = ', random_name)

if names_dict.get(random_name) == "female":
    if random_name in ["Полина", "Анна", "Дарья"]:
        random_name = random_name + '-' + random_name
        print(f'{random_name} - это девочка')
    else:
        print(f'{random_name} - это девочка')
elif names_dict.get(random_name) == "male":
    if random_name.startswith("М"):
        print(f'{random_name} - это мальчик на букву М')
    else:
        print(f'{random_name} - этот мальчик не на букву М')
else:
    print(f'{random_name} - это третий гендер или опечатка')


# 5. взять 2 переменных. Если в каждой переменной лежит тип int - вывести их сумму.

x5, y5 = random.choice([int(random.uniform(0,10)),round(random.uniform(0,10),2)]), random.choice([int(random.uniform(0,10)),round(random.uniform(0,10),2)])

print('x5, y5 = ', x5, y5)

if (type(x5) == int) and (type(y5) == int):
    summa = x5 + y5
    print('summa = x5 + y5 = ', summa)
else:
    print('Они не ОБА int')
# print(int(7.476871666967963))


# 6. использовать оператор if с типом list - проверить наличие значения в списке.

if input() in string.ascii_letters:
    print('Its a part of ascii alphabet')
else:
    print('Its DERENATLY NOT part of ascii alphabet')
