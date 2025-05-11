import yaml

people = [
    {'name': 'Анна', 'age': 28, 'city': 'Москва'},
    {'name': 'Иван', 'age': 35, 'city': 'Санкт-Петербург'},
    {'name': 'Ольга', 'age': 22, 'city': 'Новосибирск'}
]

with open(r'yaml_people_list_DZ.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data=people, stream=file, allow_unicode=True)