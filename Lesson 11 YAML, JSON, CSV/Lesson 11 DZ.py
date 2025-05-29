import yaml

import json

import pandas as pd

# people = [
#     {'name': 'Анна', 'age': 28, 'city': 'Москва'},
#     {'name': 'Иван', 'age': 35, 'city': 'Санкт-Петербург'},
#     {'name': 'Ольга', 'age': 22, 'city': 'Новосибирск'}
# ]
#
# with open(r'yaml_people_list_DZ.yaml', 'w', encoding='utf-8') as file:
#     yaml.dump(data=people, stream=file, allow_unicode=True)
#
#
# with open('yaml_people_list_DZ.yaml', 'r', encoding='utf-8') as file:
#     people_data_load = yaml.load(stream=file, Loader=yaml.FullLoader)
#     print(people_data_load)
#     print(type(people_data_load))
#
#
# with open('json_people_list_DZ.json', 'w', encoding='utf-8') as file:
#     json.dump(obj=people, fp=file, ensure_ascii=False, indent=4)
#     print(people)

data_chat_gpt = {
    'Name': ['Иван', 'Мария', 'Пётр'],
    'Age': [28, 34, 45],
    'City': ['Москва', 'Санкт-Петербург', 'Новосибирск']
}

data_to_save = pd.DataFrame(data_chat_gpt)

print(data_to_save)
print(type(data_to_save))

data_to_save.to_csv(path_or_buf='Pandas_dataframe_read_test.csv', index=False)