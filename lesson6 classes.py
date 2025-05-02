class Human:
    def __init__(self, name):
        self.body = 1
        self.hand = 2
        self.head = 1
        self.leg = 2
        self.eye = 2
        self.finger = 20
        self.name = name
        self.ear = 2


    def die(self):
        self.body = 0
        self.head = 0
        self.hand = 0
        self.leg = 0
        self.eye = 0
        self.finger = 0
        self.name = self.name + ' умер уже давно'
        self.ear = 0


class Dog:
    def __init__(self, name):
        self.leg = 4
        self.goodness = 'very good'
        self.tail = 1
        self.ear = 2
        self.nose = 1
        self.name = name

    def bark(self):
        if self.leg > 0 or self.tail > 0 or self.ear > 0 or self.nose > 0:
            print('Bark !!!')
            if self.leg > 0:
                self.leg -= 1
            elif self.tail > 0:
                self.tail -= 1
            elif self.ear > 0:
                self.ear -= 1
            elif self.nose > 0:
                self.nose -= 1
        else:
            print('Dog is dead !!!')


class Mouse:
    def __init__(self, name, brand, add_button):
        self.name = name
        self.brand = brand
        self.left_button = 1
        self.right_button = 1
        self.wheel = 1
        self.add_button = add_button

    def click(self):
        print(f'Mouse {self.name} Clicked !!!')

class Bus:
    def __init__(self, passenger_list=None):
        self.wheals = 4
        self.driver = 1
        self.corpus = 1
        self.passenger_list = passenger_list if passenger_list is not None else []

    def add_passenger(self, passenger_input):
        if type(passenger_input) == str:
            self.passenger_list.append(passenger_input)
        elif type(passenger_input) == list:
            self.passenger_list.extend(passenger_input)
        else:
            raise TypeError

    def remove_passanger(self, passanger_list_for_exit):
        if type(passanger_list_for_exit) == str:
            try:
                self.passenger_list.remove(passanger_list_for_exit)
            except ValueError:
                print(f'Пассажира {passanger_list_for_exit} нет в списке пассажиров!!!')
        elif type(passanger_list_for_exit) == list:
            for item in passanger_list_for_exit:
                try:
                    self.passenger_list.remove(item)
                except ValueError:
                    print(f'Пассажир {item} не найден в автобусе!!!')
        else:
            raise TypeError

    def change_all_kids_seats(self, new_seat):
        for item in self.passenger_list:
            item.change_seat(new_seat)



class Child(Human):
    def __init__(self, name, stupidity='high',weight_kg=10, seat_number=None):
        super().__init__(name)
        self.stupidity = stupidity
        self.weight_kg = weight_kg
        self.seat_number = seat_number #На данный момент ребенок может сидеть на месте, на котором уже сидит другой ребенок)вуа

    def burp(self):
        print(f'{self.name} burped all over the place. Clean it up!!!')

    def change_seat(self, desiered_seat_number):
        self.seat_number = desiered_seat_number #Нет проверки на то, сидит ли кто на этом месте уже)

    def show_seat_number(self):
        print(f'Ребенок {self.name} сидит на крелсе {self.seat_number}')

class Boy(Child):
    def __init__(self, name, power=1, respect=10):
        super().__init__(name, stupidity='high', weight_kg=10, seat_number=None)
        self.power = power
        self.respect = respect

    def fight(self, opponent=None):
        if isinstance(opponent, Boy):
            self.power += 1
            opponent.power += 1
            opponent.respect += 1
        elif isinstance(opponent, Girl):
            self.respect -= 3
            opponent.beuaty += 1


class Girl(Child):
    def __init__(self, name, beuaty=1):
        super().__init__(name, stupidity='high', weight_kg=10, seat_number=None)
        self.beuaty = beuaty

    def fight(self, opponent=None):
        self.beuaty -= 1
        opponent.beuaty -= 1

o_petya = Human('Petya')
o_sharik = Dog('Sharik')
print('o_petya.body = ', o_petya.body)
print('o_petya.name = ', o_petya.name)
o_petya.die()
print('o_petya.body = ', o_petya.body)
print('o_petya.name = ', o_petya.name)

o_sharik.bark()

for item in range(10):
    o_sharik.bark()
    print(o_sharik.leg, o_sharik.tail, o_sharik.ear, o_sharik.nose)


o_mouse_logitech = Mouse(name='Pusya', brand='logitech', add_button='emogie button')

o_mouse_logitech.click()

for item in range(5):
    o_mouse_logitech.click()

o_child_Kork = Child('Kork',stupidity='medium',weight_kg=114)


o_child_Kork.burp()

o_child_Kork_parametrs_list = [
    'name',
    'stupidity',
    'weight_kg',
    'body',
    'hand',
    'head',
    'leg',
    'eye',
    'finger',
    'ear',
]

o_child_Kork_parametrs_dict = {}

for item in o_child_Kork_parametrs_list:
    o_child_Kork_parametrs_dict[item] = getattr(o_child_Kork, item, f'ERROR!!!! Parametr <{item}> doesnt exist!' )

print(o_child_Kork_parametrs_list)
print(o_child_Kork_parametrs_dict)

# 4. Создайте класс "автобус". В автобусе должно содержаться несколько "детей" - например в list.
# Для класса автобус напишите методы добавления ребёнка в автобус, удаления ребёнка из автобуса.
print('4--' * 50 +'4')




o_Scool_bus = Bus(['Bobby','Lisa'])

print(o_Scool_bus.passenger_list)

o_Scool_bus.add_passenger('Karl')

print(o_Scool_bus.passenger_list)

o_Scool_bus.add_passenger(['John','Kauker'])

print(o_Scool_bus.passenger_list)

o_Scool_bus.remove_passanger('John')

print(o_Scool_bus.passenger_list)

o_Scool_bus.add_passenger(['John'])

print(o_Scool_bus.passenger_list)

o_Scool_bus.remove_passanger(['John','Kauker'])

print(o_Scool_bus.passenger_list)

o_Scool_bus.add_passenger(['John','Kauker'])

print(o_Scool_bus.passenger_list)

o_Scool_bus.remove_passanger(['Johan','Maximus'])

# 5. У каждого ребёнка сделайте хранение его текущего местоположения и методы для его изменения/отображения.
# У автобуса сделайте метод - при вызове которого будет меняться местоположение у всех детей,
# кто в нём находится на заданное (новое положение передавать в метод изменения положения)

o_child_Gron = Child(name='Gron', stupidity='medium',weight_kg=100, seat_number=0)
o_child_Yorn = Child(name='Yorn', stupidity='High',weight_kg=10, seat_number=1)
o_child_Kabol = Child(name='Kabol', stupidity='Low',weight_kg=1001, seat_number=2)
o_child_Pandus = Child(name='Pandus', stupidity='Zero',weight_kg=12, seat_number=3)

o_Scool_bus_2 = Bus()

print(o_Scool_bus_2.passenger_list)

input_for_passanger_list = [o_child_Gron, o_child_Yorn, o_child_Kabol, o_child_Pandus]

for item in input_for_passanger_list:
    o_Scool_bus_2.passenger_list.append(item)

print(o_Scool_bus_2.passenger_list)

o_child_Gron.change_seat(1)

o_child_Gron.show_seat_number()

o_child_Gron.change_seat(0)

o_child_Gron.show_seat_number()

o_child_Gron.burp()

o_Scool_bus_2.change_all_kids_seats(10)

o_child_Gron.show_seat_number()
o_child_Yorn.show_seat_number()
o_child_Kabol.show_seat_number()
o_child_Pandus.show_seat_number()

# o_Scool_bus_2.change_all_kids_seats(input('ВВедите номер места, куда пересадить детей: '))

o_child_Gron.show_seat_number()
o_child_Yorn.show_seat_number()
o_child_Kabol.show_seat_number()
o_child_Pandus.show_seat_number()

o_boy_Mark = Boy(name='Mark',power=2)
o_girl_Betta = Girl(name='Betta',beuaty=2)
o_boy_Pandus = Boy(name='Pandus',power=3)
o_girl_Dorina = Girl(name='Dorina',beuaty=5)

print('o_boy_Mark.power,o_boy_Pandus.power = ',o_boy_Mark.power,o_boy_Pandus.power,'|',o_boy_Mark.respect,o_boy_Pandus.respect)

o_boy_Mark.fight(o_boy_Pandus)

print('o_boy_Mark.power,o_boy_Pandus.power = ',o_boy_Mark.power,o_boy_Pandus.power,'|',o_boy_Mark.respect,o_boy_Pandus.respect)

print('o_girl_Betta, o_girl_Dorina = ', o_girl_Betta.beuaty,o_girl_Dorina.beuaty)

o_girl_Betta.fight(o_girl_Dorina)

print('o_girl_Betta, o_girl_Dorina = ', o_girl_Betta.beuaty,o_girl_Dorina.beuaty)

o_girl_Dorina.fight(o_girl_Dorina)

print('o_girl_Betta, o_girl_Dorina = ', o_girl_Betta.beuaty,o_girl_Dorina.beuaty)

print('o_boy_Pandus, o_girl_Betta = ', o_boy_Pandus.power,o_boy_Pandus.respect,'|',o_girl_Betta.beuaty)

o_boy_Pandus.fight(o_girl_Betta)

print('o_boy_Pandus, o_girl_Betta = ', o_boy_Pandus.power,o_boy_Pandus.respect,'|',o_girl_Betta.beuaty)