from Utils2.Human import Human

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