import pandas as pd

def read_csv(filename):
    try:
        input_data = pd.read_csv(filename)
        print(input_data)
    except Exception as e:
        print(f'Ошибка при чтении csv: {e}')

def save_to_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(path_or_buf=filename, index=False, encoding='utf-8')
        print(f'Dataframe сохранен в {filename}')
    except Exception as e:
        print(e)

def get_currency_by_city(filemname, city_name):
    """
    Получает валюту по для города из csv таблицы, вида:
        city,currency
        Moscow,RUB
        Saint Petersburg,RUB
    :param filemname: имя файла-таблицы .csv
    :param city_name: Имя города Moscow на английском
    :return: международный код валюты (прим. RUB)
    """
    try:
        df = pd.read_csv(filemname) #Читаем csv стандартной командой пандаса
        curr = df[df['city'].str.lower() == city_name.lower()]['currency'].values[0]  # df[]выдает из датафрейма все строки, которые положительны утверждению в скобках
        #curr2 = df[df['city'].str.lower() == city_name.lower()].iloc[0]['currency'] #честно не знаю чем отличается работают строки одинаково
        return curr

    except Exception as e:
        print(f'Произошла ошибка при поиске валюты Города {city_name}: {e}')
        return None

