import json
from datetime import datetime, timedelta
import pandas as pd

import requests

def generate_date_range(start_date_str, end_date_str): # Делает список из дат от начальной до конечной
    #Парсим входные даты из str в объекты datetime
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    current_date = start_date
    dates = []

    while current_date <= end_date:
        dates.append(current_date.strftime("%Y-%m-%d")) # Форматируем дату в строку
        current_date += timedelta(days=1) # Прибавляем 1 день

    return dates


#Мой личный ключ API на сайте exchangerate-api.com
ACCESS_KEY = '2ca22c0dcc9e3762f0040ff08dd264b8'

#4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года - и записать в 1 csv файл в 3 колонки:
#Дата Валюта Курс к доллару
start_date = '2023-11-01' #YYYY-MM-DD
end_date = '2023-11-30' #YYYY-MM-DD
source_currency = 'USD' #Через какую валюту рассчитываем
get_currency = 'EUR,RUB' # не совсем по заданию, но я по другому сделаю, потому что в бесплатном тарифе source только EUR

dates = generate_date_range(start_date, end_date) #Делаем список из всех нужных дат
print(dates)
# Наша ссылка по которой переходим

rows = [] #Сюда сохраняем все данные из json

for date in dates:
    URL = f'http://api.currencylayer.com/historical?access_key={ACCESS_KEY}&date={date}&source={source_currency}&currencies={get_currency}&format=1'
    response = requests.get(URL)
    data = response.json()

    if data.get("success"): #Есть получение json или нет
        quotes = data.get("quotes", {})  #Из API курсы внутри "quotes" хранятся
        for currency_code in get_currency.split(','): #Для каждой валюты получаем данные
            pair = source_currency + currency_code #В "quotes" курс хранится по ключу типа "USDEUR"
            rate = quotes.get(pair) #Получаем курс цифрой
            if rate is not None:
                rows.append({'Дата':date, 'Валюта':currency_code, 'Курс к доллару':rate})


    else:
        print(f'Ошибка на дату {date}: Код ошибки {data.get("error")}')

df = pd.DataFrame(rows) #Создаем Dataframe из списочка, который получили из json
df.to_csv(path_or_buf=f'Курс валют {start_date} - {end_date}.csv', index=False, encoding='utf-8')
print(f'Курс валют {start_date} - {end_date}.csv сохранен')

# Сохраняем json для проверки
# with open('api_currencylayer_historical_2023-11-01_test.json', 'w', encoding='utf-8') as file:
#     json.dump(obj=data, fp=file, ensure_ascii=False, indent=4)
# print(data)