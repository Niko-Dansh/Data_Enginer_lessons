import yaml
import json
import pandas as pd


# 3. Создать класс, в классе хранить лист словарей
# (как у меня в коде пример с подключениями - можете придумать что-нибудь своё,
# например в словарях данные людей будут или ещё что-нибудь)
class Datum:
    def __init__(self):
        self.df = pd.DataFrame()
        self.list_of_dicts =  []

    # 4. Сделать 2 метода для работы с YAML - для сохранения в файл и для чтения из файла.
    # Название фала должно передаваться в метод входным параметром.
    def yaml_read(self, filename, add=False, return_data=False): #here name is a name for a file to read, add- to add data to list_of_dicts
        try:
            with open(filename,'r', encoding='utf-8') as file:
                input_data = yaml.load(stream=file, Loader=yaml.FullLoader)
                print(input_data)
                if add:
                    self.list_of_dicts.append(input_data)
                    print('New data added to <list_of_dicts>')
                if return_data:
                    return input_data
        except Exception as e:
            print(e)

    def yaml_save(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                yaml.dump(data=self.list_of_dicts, stream=file, allow_unicode=True)
        except Exception as e:
            print(e)

    # 5. Сделать 2 метода для работы с JSON - для сохранения в файл и для чтения из файла.
    # Название фала должно передаваться в метод входным параметром.
    def json_read(self, filename, add=False):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                input_data = json.load(file)
                print(input_data)
                if add:
                    self.list_of_dicts.extend(input_data)
        except Exception as e:
            print(e)

    def json_save(self, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(obj=self.list_of_dicts, fp=file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)

    # 6. В другом поле хранить Pandas DataFrame с данными.
    # Написать ещё 2 метода - для сохранения данных в файл .csv и для чтения данных из .csv файла в датафрейм.

    def csv_read(self, filename, add=False):
        try:
            input_data = pd.read_csv(filename)
            print(input_data)
            if add:
                self.df = pd.concat([self.df, input_data], ignore_index=True)
        except Exception as e:
            print(f'Ошибка при чтении csv: {e}')

    def csv_save(self, filename):
        try:
            self.df.to_csv(path_or_buf=filename, index=False, encoding='utf-8')
            print(f'Dataframe сохранен в {filename}')
        except Exception as e:
            print(e)

    """
    Так же написать для 4, 5, 6 пунктов методы, которые будут просто отображать данные, которые внутри объекта хранятся.
    
    :return: 
        данные из self.list_of_dicts в нужном формате
    """
    @property
    def yaml_data(self):
        return yaml.dump(data=self.list_of_dicts, allow_unicode=True)

    @property
    def json_data(self):
        """
        Геттер для данных всего класса Datum
        :return: json строка
        """
        return json.dumps(obj=self.list_of_dicts, ensure_ascii=False, indent=4)

    @property
    def dataframe(self):
        """
        Геттер для данных отдельного экземпляра класса Datum
        :return: Pandas DataFrame
        """
        return self.df

    def print_all(self):
        """
        Печатает все данные из общеклассового списка <list_of_dicts>

        Выводит в консоль строки с индексом и содержимым каждого словаря

        :return:
            None
        """
        for i, item in enumerate(self.list_of_dicts, start=1):
            print(f'{i}: {item}')


Datum_test = Datum()

Datum_test.yaml_read('YAML_read_test.yaml')
Datum_test.yaml_save('Datum_test_yaml_save.yaml')
Datum_test.yaml_read('Datum_test_yaml_save.yaml')

Datum_test.yaml_read('YAML_read_test.yaml',add=True)
Datum_test.yaml_save('Datum_test_yaml_save_after_adding.yaml')
Datum_test.yaml_read('Datum_test_yaml_save_after_adding.yaml')

Datum_test.print_all()
print('-' * 100)
Datum_test.json_read(filename='json_people_list_DZ.json')
print('-' * 100)
Datum_test.json_read(filename='json_people_list_DZ.json',add=True)
Datum_test.print_all()
Datum_test.json_save('json_people_list_save_after_adding_DZ.json')
print('-' * 100)
print(Datum_test.list_of_dicts)
print('-' * 100)
Datum_test_2 = Datum()

print('Datum_test_2', Datum_test_2.list_of_dicts)
print('-' * 100)

print(Datum_test_2.df)
print('-' * 100)

Datum_test_2.csv_read('Pandas_dataframe_read_test.csv')
Datum_test_2.csv_read('Pandas_dataframe_read_test.csv', add=True)
print('-' * 100)
print(Datum_test_2.df)

Datum_test_2.csv_save('Datum_test_2_pandas_dataframe.csv')
print('-' * 100)

Datum_test_2.csv_read('Datum_test_2_pandas_dataframe.csv')
print('-' * 100)
Datum_test.print_all()
print('-' * 100)
Datum_test_2.print_all()

print('-' * 100)

print(Datum_test.yaml_data)
print(Datum_test.json_data)
print(Datum_test_2.dataframe)
print('-' * 100)
# 7. Попробовать при помощи объекта класса прочитать данные из YAML формата, а сохранить - в JSON.
o_YAML_to_JSON = Datum()
o_YAML_to_JSON.yaml_read('YAML_read_test.yaml',add=True, return_data=False)
o_YAML_to_JSON.json_save('YAML_to_JSON_conv.json')
print('-' * 100)

# 8. Наоборот: прочитать данные из JSON, сохранить в YAML.
o_JSON_to_YAML = Datum()
o_JSON_to_YAML.json_read('json_people_list_DZ.json', add=True)
o_JSON_to_YAML.yaml_save('JSON_to_YAML_conv.yaml')

