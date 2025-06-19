# Сопоставление городов к странам и валютам
currency_map = {
    "Russia": "RUB",
    "Kazakhstan": "KZT",
    "Ukraine": "UAH",
    "Belarus": "BYN",
    "Israel": "ILS",
    "USA": "USD"
}

# Города с указанием страны (чтобы правильно определить валюту)
city_country_map = {
    # Россия
    "Moscow": "Russia",
    "Saint Petersburg": "Russia",
    "Novosibirsk": "Russia",
    "Yekaterinburg": "Russia",
    "Nizhny Novgorod": "Russia",
    "Kazan": "Russia",
    "Chelyabinsk": "Russia",
    "Omsk": "Russia",
    "Samara": "Russia",
    "Rostov-on-Don": "Russia",
    "Ufa": "Russia",
    "Krasnoyarsk": "Russia",
    "Voronezh": "Russia",
    "Perm": "Russia",
    # Казахстан
    "Almaty": "Kazakhstan",
    "Nur-Sultan": "Kazakhstan",
    "Shymkent": "Kazakhstan",
    "Karaganda": "Kazakhstan",
    "Aktobe": "Kazakhstan",
    # Украина
    "Kyiv": "Ukraine",
    "Kharkiv": "Ukraine",
    "Odesa": "Ukraine",
    "Dnipro": "Ukraine",
    "Donetsk": "Ukraine",
    # Беларусь
    "Minsk": "Belarus",
    "Gomel": "Belarus",
    "Mogilev": "Belarus",
    "Vitebsk": "Belarus",
    "Grodno": "Belarus",
    # Израиль
    "Tel Aviv": "Israel",
    "Jerusalem": "Israel",
    "Haifa": "Israel",
    "Rishon LeZion": "Israel",
    "Petah Tikva": "Israel",
    # США
    "New York": "USA",
    "Los Angeles": "USA",
    "Chicago": "USA",
    "Houston": "USA",
    "Philadelphia": "USA"
}

# Формируем список словарей с городом и валютой
cities_with_currency = []
for city in city_country_map:
    country = city_country_map[city]
    currency = currency_map.get(country, "Unknown")
    cities_with_currency.append({"city": city, "currency": currency})

# Пример вывода
print(cities_with_currency)