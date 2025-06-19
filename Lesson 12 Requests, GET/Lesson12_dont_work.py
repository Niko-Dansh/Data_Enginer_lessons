import requests

#Мой личный ключ API на сайте exchangerate-api.com
ACCESS_KEY = '2ca22c0dcc9e3762f0040ff08dd264b8'


#4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года
start_date = '2023/11/01' #YYYY-MM-DD
end_date = '2023/11/31' #YYYY-MM-DD
source_currency = 'USD'
get_currency = 'EUR,RUB' #str международные коды без пробелов через запятую

# Наша ссылка по которой переходим
URL = f'http://api.currencylayer.com/timeframe?access_key={ACCESS_KEY}&start_date={start_date}&end_date={end_date}&source={source_currency}&currencies={get_currency}&format=1'

#получаем ответ от АПИ
response = requests.get(URL)

#Преобразуем джейсончик в список словарей или как-то так...
data = response.json()

#Печатаем наш ответ
print(data)

import requests


#Мой личный ключ API на сайте exchangerate-api.com
api_key = '144643dfd5335cc456af64e8'


#4. Получить курс рубля к доллару и евро к доллару за каждый день ноября 2023 года
start_date = '2023/11/01'
end_date = '2023/11/31'


# Наша ссылка по которой переходим
URL = f'https://v6.exchangerate-api.com/v6/{api_key}/history/USD/2023/11/01'

#получаем ответ от АПИ
response = requests.get(URL)

#Преобразуем джейсончик в список словарей или как-то так...
data = response.json()

#Печатаем наш ответ
print(data)

