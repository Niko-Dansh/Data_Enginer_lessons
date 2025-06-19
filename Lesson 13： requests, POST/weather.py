import requests

def get_city_weather(city_input):
    try:
        api_key ='4a175d44b9ad4d78be3111745250806'
        URL_city_current = f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_input}&aqi=no'
        data_city_current = requests.get(URL_city_current ).json()
        temp_c = data_city_current.get("current", {}).get("temp_c", 'нет данных')
        feelslike_c = data_city_current.get("current", {}).get("feelslike_c", 'нет данных')
        condition_text = data_city_current.get("current", {}).get("condition", {}).get("text", 'нет данных')
        pressure_mb = data_city_current.get("current", {}).get("pressure_mb", 'нет данных')
        pressure_mmHg = round(pressure_mb * 0.75006)
        uv = data_city_current.get("current", {}).get("uv", 'нет данных')

        return f'''Погода в {city_input}: {condition_text}
        Температура {temp_c}, С°
        Чувствуется как {feelslike_c}, С°
        Давление {pressure_mmHg} мм рт.ст.
        УФ-индекс {uv}'''

    except Exception as e:
        print(e)