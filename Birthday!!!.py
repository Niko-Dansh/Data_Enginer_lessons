Список_приглашений = [
    'Я',
    'Настюша',
    'Сестра Аня',
    'Муж Ани Коля',
    'Папа Саша',
    'Мама Люда',

    'Подруга Насти новая',
    'Лучший друг Влад',
    'Гурген',
    'Паша - да я Паша'
    'Друг 2 Алексахин Павел',
    ]

список_приглашений_Final = [Список_приглашений[0], Список_приглашений[1], Список_приглашений[2], Список_приглашений[4], Список_приглашений[5], Список_приглашений[6]]

Список_приглашений_длинна =len(Список_приглашений)
Список_дел_текущий = [
    'Что по подаркам - вишлист',
    'Понять кто придет - Число людей',
    'Прикинуть сколько денег надо',
    '',
]

план_дня_рождения = {
    'Собираемся в Крюково': '12:30',
    'Прибытие на каток': '14:00',
    'Катание на катке': '14:00 - 16:00',
    'Кушание в ресторане': '16:00 - 18:00',
    'Зайти в рок магазин': '18:00 - 19:00',
    'Погулять по ВДНХ': '?????',
    '': '',
    '': '',
}


for var_name, var_value in locals().copy().items():
    if any(var_name.startswith(letter) for letter in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'):
        print(f'{var_name} = {var_value}')

