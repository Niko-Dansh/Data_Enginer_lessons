import requests
import json
"""

Я, например, сделал тг бота для получения погоды по апи и сохранения данных в csv и SQLAlchemy
Этот вопрос наверное самый популярный в курсе
TsMark01/RocketGroot
https://github.com/TsMark01/RocketGroot/tree/main
Вот если интересно код
Я: Фига ты монстр. Получается мне самому просто что-то придумать и сделать на коленке? окей
Типа такого же, что сделал я
Попробую сделать интегрирования двух апи
Например по погоде
И курсу доллара
Не надо в тг боте делать - там тоже свой синтаксис, сделай через консоль
Типа принт" Я ваш помощник, что вы хотите получить сегодня. 1. Погода 2. Курс доллара"
Сделай проверку на ввод именно этих числе и реализуй функции по апи, их вызывай при 1 или 2

"""


#Мой личный ключ API на сайте exchangerate-api.com и weatherapi.com
ACCESS_KEY = '2ca22c0dcc9e3762f0040ff08dd264b8'
weatherapi_com ='4a175d44b9ad4d78be3111745250806'

#Получить для Москвы на 1 день, сохранить в json
URl_Moscow_current = 'https://api.weatherapi.com/v1/current.json?key=4a175d44b9ad4d78be3111745250806&q=Moscow&aqi=no'
response_URl_Moscow_current = requests.get(URl_Moscow_current)
data_URl_Moscow_current = response_URl_Moscow_current.json()
# print('Код ответа',response_URl_Moscow_current.status_code)
# print('Текст ответа',response_URl_Moscow_current.text)

# with open('json archive/Moscow_current_weather.json', 'w', encoding='utf-8') as file:
#     json.dump(data_URl_Moscow_current, file, ensure_ascii=False, indent=4 )


#сформировать список городов из моего списка и проверить их все на получение погоды
cities = [
    # Россия
    "Moscow",
    "Saint Petersburg",
    "Novosibirsk",
    "Yekaterinburg",
    "Nizhny Novgorod",
    "Kazan",
    "Chelyabinsk",
    "Omsk",
    "Samara",
    "Rostov-on-Don",
    "Ufa",
    "Krasnoyarsk",
    "Voronezh",
    "Perm",
    # Казахстан
    "Almaty",
    "Nur-Sultan",
    "Shymkent",
    "Karaganda",
    "Aktobe",
    # Украина
    "Kyiv",
    "Kharkiv",
    "Odesa",
    "Dnipro",
    "Donetsk",
    # Беларусь
    "Minsk",
    "Gomel",
    "Mogilev",
    "Vitebsk",
    "Grodno",
    # Израиль
    "Tel Aviv",
    "Jerusalem",
    "Haifa",
    "Rishon LeZion",
    "Petah Tikva",
    # США
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Philadelphia"
]

"""
сделал и деактивировал эту функцию 

for city in cities:
    URl_city_current = f'https://api.weatherapi.com/v1/current.json?key=4a175d44b9ad4d78be3111745250806&q={city}&aqi=no'
    response_URl_city_current = requests.get(URl_city_current)
    data_URl_city_current = response_URl_city_current.json()
    with open(f'json archive/{city}_curr.json', 'w', encoding='utf-8') as file:
        json.dump(data_URl_city_current, file, ensure_ascii=False, indent=4)
"""

#создать базу данных с городами и валютами к ним - те, что по моему списку
cities_with_currency = [
    # Россия
    {"city": "Moscow", "currency": "RUB"},
    {"city": "Saint Petersburg", "currency": "RUB"},
    {"city": "Novosibirsk", "currency": "RUB"},
    {"city": "Yekaterinburg", "currency": "RUB"},
    {"city": "Nizhny Novgorod", "currency": "RUB"},
    {"city": "Kazan", "currency": "RUB"},
    {"city": "Chelyabinsk", "currency": "RUB"},
    {"city": "Omsk", "currency": "RUB"},
    {"city": "Samara", "currency": "RUB"},
    {"city": "Rostov-on-Don", "currency": "RUB"},
    {"city": "Ufa", "currency": "RUB"},
    {"city": "Krasnoyarsk", "currency": "RUB"},
    {"city": "Voronezh", "currency": "RUB"},
    {"city": "Perm", "currency": "RUB"},

    # Казахстан
    {"city": "Almaty", "currency": "KZT"},
    {"city": "Nur-Sultan", "currency": "KZT"},
    {"city": "Shymkent", "currency": "KZT"},
    {"city": "Karaganda", "currency": "KZT"},
    {"city": "Aktobe", "currency": "KZT"},

    # Украина
    {"city": "Kyiv", "currency": "UAH"},
    {"city": "Kharkiv", "currency": "UAH"},
    {"city": "Odesa", "currency": "UAH"},
    {"city": "Dnipro", "currency": "UAH"},
    {"city": "Donetsk", "currency": "UAH"},

    # Беларусь
    {"city": "Minsk", "currency": "BYN"},
    {"city": "Gomel", "currency": "BYN"},
    {"city": "Mogilev", "currency": "BYN"},
    {"city": "Vitebsk", "currency": "BYN"},
    {"city": "Grodno", "currency": "BYN"},

    # Израиль
    {"city": "Tel Aviv", "currency": "ILS"},
    {"city": "Jerusalem", "currency": "ILS"},
    {"city": "Haifa", "currency": "ILS"},
    {"city": "Rishon LeZion", "currency": "ILS"},
    {"city": "Petah Tikva", "currency": "ILS"},

    # США
    {"city": "New York", "currency": "USD"},
    {"city": "Los Angeles", "currency": "USD"},
    {"city": "Chicago", "currency": "USD"},
    {"city": "Houston", "currency": "USD"},
    {"city": "Philadelphia", "currency": "USD"}
]

#написать код, который дает запрос по данным сегодня по погоде и курсу валют для города
city_input = input('Введите город - получите погоду и курс местной валюты : ').title() #вводим данные - делаем с большой буквы каждое слово

#получить для введенного города погоду и напечатать
'''
URl_input_city_current = f'https://api.weatherapi.com/v1/current.json?key=4a175d44b9ad4d78be3111745250806&q={city_input}&aqi=no'
response_URl_input_city_current = requests.get(URl_input_city_current)
data_URl_input_city_current = response_URl_input_city_current.json()
print(f'Погода в {city_input}:')
print(data_URl_input_city_current)
'''
#получить для введенного города валюту курс и напечатать
'''
city_to_currency = {entry['city']: entry['currency'] for entry in cities_with_currency}#преоб. в словарь для поиска
access_key = '2ca22c0dcc9e3762f0040ff08dd264b8'
source = 'USD' #city_to_currency.get(city_input) только для платных клиентов(
currencies = f"{city_to_currency.get(city_input)},EUR,RUB"

url_input_city_curr = f"http://api.currencylayer.com/live?access_key={access_key}&currencies={currencies}&source={source}&format=1"
print(url_input_city_curr)
response_curr = requests.get(url_input_city_curr)
data_curr = response_curr.json()
print(f'Курс валют в {city_input}: ')
print(data_curr)
'''

#написать код, как предыдущий, но выдаем только строки погода:температура, температура по ощущению, погода в целом(типо дождь), давление, uv
# по курсу валют написать кратенько курс валюты города к доллару, потом евро и рубль
#Запрашивать вариант сохранения в csv через пандас
save_to_csv = True if input('Сохранить в CSV?(Y/N): ').lower() == 'y' else False
URL_179_city_curr = f'https://api.weatherapi.com/v1/current.json?key=4a175d44b9ad4d78be3111745250806&q={city_input}&aqi=no'
data_179_city_curr = requests.get(URL_179_city_curr).json()
temp_c = data_179_city_curr.get("current", {}).get("temp_c", 'нет данных')
feelslike_c = data_179_city_curr.get("current", {}).get("feelslike_c", 'нет данных')
condition_text = data_179_city_curr.get("current", {}).get("condition", {}).get("text", 'нет данных')
pressure_mb = data_179_city_curr.get("current", {}).get("pressure_mb", 'нет данных')
pressure_mmHg = round(pressure_mb * 0.75006)
uv = data_179_city_curr.get("current", {}).get("uv", 'нет данных')
print(f'''Погода в {city_input}: {condition_text}
Температура {temp_c}, С°
Чувствуется как {feelslike_c}, С°
Давление {pressure_mmHg} мм рт.ст.
УФ-индекс {uv}''')

print('-' * 25) #Разделитель
city_to_currency_2 = {entry['city']: entry['currency'] for entry in cities_with_currency}
city_currency = city_to_currency_2.get(city_input)
currencies = f'{city_currency},EUR,RUB'
source = 'USD'
URL_196_city_curr = f"http://api.currencylayer.com/live?access_key={ACCESS_KEY}&currencies={currencies}&source={source}&format=1"
data_200_city_curr_quotes = requests.get(URL_196_city_curr).json().get('quotes', 'нет данных')
usd_city_curr = data_200_city_curr_quotes.get(f'USD{city_currency}')
USD_EUR = data_200_city_curr_quotes.get('USDEUR')
USD_RUB = data_200_city_curr_quotes.get('USDRUB')
print(f'''Курс валют в {city_input}:
USD/{city_currency}: {usd_city_curr}
USD/EUR: {USD_EUR}
USD/RUB: {USD_RUB}
''')

#написать код, который дает запрос по данным за последние n дней(до 14 дней - ограничение по API) по погоде и курсу валют для города



#ЗАГРУЗИТЬ НА ГИТХАБ ВСЕ ЧТО ЕСТЬ МОЮ ВЕТКУ

