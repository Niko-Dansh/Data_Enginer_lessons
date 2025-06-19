import requests


def get_currency_rates(city_currency):
    api_key = '2ca22c0dcc9e3762f0040ff08dd264b8' #Мой личный ключ API на сайте exchangerate-api.com
    currencies = f'{city_currency},EUR,RUB'
    source = 'USD'
    URL_city_curr = f"http://api.currencylayer.com/live?access_key={api_key}&currencies={currencies}&source={source}&format=1"
    data_city_curr_quotes = requests.get(URL_city_curr).json().get('quotes', 'нет данных')
    usd_city_curr = data_city_curr_quotes .get(f'USD{city_currency}')
    USD_EUR = data_city_curr_quotes .get('USDEUR')
    USD_RUB = data_city_curr_quotes .get('USDRUB')

    return {
        f'USD/{city_currency}': usd_city_curr,
        'USD/EUR': USD_EUR,
        'USD/RUB': USD_RUB
    }
