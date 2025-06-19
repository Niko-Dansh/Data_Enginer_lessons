from csv_utils import get_currency_by_city
from currency import get_currency_rates
from weather import get_city_weather

#написать код, который дает запрос по данным сегодня по погоде и курсу валют для города

city_input = input('Введите город - получите погоду и курс местной валюты : ').title() #вводим данные - делаем с большой буквы каждое слово

#Получить из таблицы городов код валюты и напечатать 1 раз затем хранить как переменную
city_input_curr = get_currency_by_city('data/cities_with_currency.csv', city_input) #получаем данные кода валюты

currency_rates_dict = get_currency_rates(city_input_curr) #получаем словарь с курсами валют по апи
print(f'Курс валют в {city_input}:')
for key, value in currency_rates_dict.items():
    print(f'{key}: {value}')

print('-' * 25) #Разделитель

city_input_weather = get_city_weather(city_input)
print(city_input_weather)
