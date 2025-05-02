from Utils2.Rota import  Rota

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
