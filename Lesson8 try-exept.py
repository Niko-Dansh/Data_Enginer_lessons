def CountCharactersInText(text):
    count_dict={}
    for char in text:
        try:
            count_dict[char] += 1
        except KeyError:
            count_dict[char] = 1
    return count_dict

text_1 = 'abcde'

print(CountCharactersInText('abcde'))


class Human():
    def __init__(self, name='Mihail',surname='Smirnov',age='39'):
        self.human_body = 1
        self.name = name
        self.surname = surname
        self.age = age
        self.rota = None
        self.polk = None

    def set_rota(self, new_rota):
        self.rota = new_rota

    def set_polk(self, new_polk):
        self.polk = new_polk

    def __repr__(self):
        return f'Human({self.name} {self.surname}, Age: {self.age})'

    def get_info(self):
        return f'{self.name} {self.surname}, {self.age} лет'

    # def __str__(self):
    #     return 'Test what __str__ is doing'

class Rota():
    def __init__(self, rota_name='New Rota',rota_dislocation='Moscow', soldiers_list=None):
        self.name = rota_name
        self.dislocation = rota_dislocation
        self.polk = None
        if soldiers_list is None:
            self.soldiers_list = []
        elif isinstance(soldiers_list, list):
            self.soldiers_list = soldiers_list
        elif isinstance(soldiers_list, Human):
            self.soldiers_list = [soldiers_list]
        else:
            raise ValueError('В списке людей в роте должны быть ничего, объект класса <Human> или список из объектов класса <Human>')

    def add_soldier(self, new_soldier):
        if not isinstance(new_soldier, Human):
            raise ValueError("Only Human instances can be added")
        self.soldiers_list.append(new_soldier)
        new_soldier.set_rota(self)
        new_soldier.set_polk(self.polk)

    def remove_soldiers(self, list_of_soldiers_for_removal):
        if not isinstance(list_of_soldiers_for_removal, list):
            raise ValueError('<list_of_soldiers_for_removal> must be <list>')
        for item in list_of_soldiers_for_removal:
            try:
                self.soldiers_list.remove(item)
                item.set_rota(None)
                item.set_polk(None)
            except Exception:
                print('Problem!!!!')

    def set_polk(self, new_polk):
        self.polk = new_polk

    def get_soldiers_info(self):
        return self.soldiers_list

    def __repr__(self):
        return f'Rota(Name: {self.name}, Dislocation: {self.dislocation}, Soldiers: {len(self.soldiers_list)})'


class Polk:
    def __init__(self, polk_name='Moscowski', polk_dislocation='Moscow', rota_list=None):
        self.name = polk_name
        self.dislocation = polk_dislocation
        if rota_list is None:
            self.rota_list = []
        elif isinstance(rota_list, Rota):
            self.rota_list = [rota_list]
        elif isinstance(rota_list, list):
            for item in rota_list:
                if not isinstance(item, Rota):
                    raise ValueError('В списке людей в полку должны быть ничего, объект класса <Rota> или список из объектов класса <Rota>')
                self.rota_list = rota_list
        else:
            raise ValueError(f'Вы ввели тип данных: {type(rota_list)}. В списке людей в полку должны быть ничего, объект класса <Rota> или список из объектов класса <Rota>')

    def __repr__(self):
        return f'Polk(Name: {self.name}, Dislocation: {self.dislocation}, Rota`s: {len(self.rota_list)})'

    def add_rota(self, new_rota):
        if not isinstance(new_rota, Rota):
            raise ValueError('Only <Rota> object can be added')
        self.rota_list.append(new_rota)
        new_rota.set_polk(self)

    def remove_rotas(self, list_of_rotas_for_removal):
        if not isinstance(list_of_rotas_for_removal, list):
            raise ValueError('<list_of_rotas_for_removal> must be <list>')
        for rota in list_of_rotas_for_removal:
            try:
                self.rota_list.remove(rota)
                rota.set_polk(None)
                for soldier in rota.soldiers_list:
                    try:
                        soldier.set_polk(None)
                    except Exception:
                        print('Problem 2!!!')
            except Exception:
                print('Problem!!!!')

    def get_all_soldiers(self):
        dict_1 = {}

        for item in self.rota_list:
            dict_1[item] = item.get_soldiers_info()

        return dict_1


o_Default_Human = Human()
o_Default_Rota = Rota()
o_Default_Polk = Polk()

print(o_Default_Human.name, o_Default_Human.surname, o_Default_Human.age)
print(o_Default_Rota.name, o_Default_Rota.dislocation, o_Default_Rota.soldiers_list)
print(o_Default_Polk.name, o_Default_Polk.dislocation, o_Default_Polk.rota_list)

o_lolkek_cheburec_Rota = Rota(rota_name='lolkek_cheburec',rota_dislocation='Sex 2', soldiers_list=['Vasya',o_Default_Human])

print(o_lolkek_cheburec_Rota.name, o_lolkek_cheburec_Rota.dislocation, o_lolkek_cheburec_Rota.soldiers_list)

o_test_Polk_1 = Polk(polk_name='Yopt', polk_dislocation='Ivanovo', rota_list=o_lolkek_cheburec_Rota)

print(o_test_Polk_1.name, o_test_Polk_1.dislocation, o_test_Polk_1.rota_list)
print(o_lolkek_cheburec_Rota.soldiers_list[1])

o_human_1 = Human(name='Ivan_1',surname='Ivanov_1', age=15)
o_human_2 = Human(name='Ivan_2',surname='Ivanov_2', age=16)
o_human_3 = Human(name='Ivan_3',surname='Ivanov_3', age=17)
o_human_4 = Human(name='Ivan_4',surname='Ivanov_4', age=18)

o_rota_1 = Rota(rota_name='Rota_1', rota_dislocation='Moscow',soldiers_list=None)
o_rota_2 = Rota(rota_name='Rota_2', rota_dislocation='Saint Petersberg',soldiers_list=None)

o_polk_0 = Polk(polk_name='Smertnitzkiy',polk_dislocation='Hell',rota_list=None)
print('-' * 100)

print(o_human_1)
print(o_human_2)
print(o_human_3)
print(o_human_4)

print(o_rota_1)
print(o_rota_2)

print(o_polk_0)

print('-' * 100)

o_polk_0.add_rota(new_rota=o_rota_1)
o_polk_0.add_rota(new_rota=o_rota_2)

print(o_polk_0)
print(o_polk_0.rota_list)

print(o_rota_1.polk)
print(o_rota_2.polk)

o_rota_1.add_soldier(o_human_1)
o_rota_1.add_soldier(o_human_2)

o_rota_2.add_soldier(o_human_3)
o_rota_2.add_soldier(o_human_4)

print(o_rota_1.soldiers_list)
print(o_rota_2.soldiers_list)

print('-' * 100)

print(o_human_1.polk)
print(o_human_2.polk)
print(o_human_3.polk)
print(o_human_4.polk)

print('-' * 100)

print(o_rota_1.soldiers_list)
o_rota_1.remove_soldiers([o_human_1, o_human_2])
print(o_rota_1.soldiers_list)

o_rota_1.add_soldier(o_human_1)
o_rota_1.add_soldier(o_human_2)
print(o_rota_1.soldiers_list)
o_rota_1.remove_soldiers([o_human_1])
print(o_rota_1.soldiers_list)
o_rota_1.add_soldier(o_human_1)
print(o_rota_1.soldiers_list)

print('-' * 100)

print(o_polk_0.rota_list)

o_polk_0.remove_rotas([o_rota_1])

print(o_polk_0.rota_list)

o_polk_0.remove_rotas([o_rota_2])

print(o_polk_0.rota_list)

print('-' * 100)

print(o_human_1.get_info())
print(o_rota_1.get_soldiers_info())

o_polk_0.add_rota(o_rota_1)
o_polk_0.add_rota(o_rota_2)
print(o_polk_0.rota_list)
print('-' * 100)
print(o_polk_0.get_all_soldiers())

