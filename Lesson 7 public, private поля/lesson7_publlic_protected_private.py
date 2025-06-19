class Alien:
    stand_and_stare_speed = 0
    walk_speed = 2
    fly_saucer_speed = 2000

    def __init__(self, name='Alien', color='Full green'):
        if not isinstance(name, str):
            raise TypeError('You inputed <name> not as a string')
        if not isinstance(color, str):
            raise TypeError('You inputed <color> not as a string')
        self.name = name
        self.color = color
        self.sex = None
        self.height_m = 1
        self.head = 1
        self.eye = 2
        self.__eye_color = 'Black'
        self.nose = None
        self.mouth = 1
        self.neck = 1
        self.hand = 2
        self.finger = 12
        self.body = 1
        self.leg = 2
        self.speed_mps = self.walk_speed
        self.__seat_number = None


    def set_alien_eye_color(self, eye_color):
        if not isinstance(eye_color, str):
            raise TypeError('Alien eye_color must be <str>')
        self.__eye_color = eye_color

    def get_alien_eye_color(self):
        return self.__eye_color

    def steal_human(self, number_of_humans_stollen):
        if not isinstance(number_of_humans_stollen, int):
            raise TypeError('Alien steal only <int> number of humans')
        else:
            self.number_of_humans_stollen = number_of_humans_stollen

    def alien_move(self, stand_and_stare=False, walk=False, fly_in_Saucer=False):
        if stand_and_stare:
            self.speed_mps = self.stand_and_stare_speed
        if walk:
            self.speed_mps = self.walk_speed
        if fly_in_Saucer:
            self.speed_mps = self.fly_saucer_speed

    def set_seat_number(self, new_seat_number):
        self.__seat_number = new_seat_number

    def get_seat_number(self):
        return  self.__seat_number


class AlienSeedling(Alien):
    def __init__(self, name='E.T.', color='green'):
        super().__init__(name, color)
        self.name = 'lil ' + name
        self.color = 'light ' + color


class Saucer():
    def __init__(self, shape='disk', saucer_flight_speed_mps=2000):
        if not isinstance(shape, str):
            raise TypeError('Alien Saucer shape is <str>')
        if not isinstance(saucer_flight_speed_mps, (int, float)):
            raise TypeError('Alien Saucer speed must be either <int> of <float>')
        self.__shape = shape
        self.__saucer_flight_speed_mps = saucer_flight_speed_mps
        self.__passanger_list_of_objects = []

    @property
    def saucer_shape(self):
        return self.__shape

    @saucer_shape.setter
    def saucer_shape(self, new_shape):
        self.__shape = new_shape

    @property
    def flight_speed(self):
        return self.__saucer_flight_speed_mps

    @flight_speed.setter
    def flight_speed(self, new_saucer_speed):
        self.__saucer_flight_speed_mps = new_saucer_speed

    def add_alien(self, pass_obj):
        if not isinstance(pass_obj, Alien):
            raise TypeError('Aliens must be an instance of the Alien class')
        if pass_obj in self.__passanger_list_of_objects:
            raise ValueError(f'Инопланетянин {pass_obj.name} уже в списке пассажиров')
        self.__passanger_list_of_objects.append(pass_obj)
        pass_obj.set_seat_number(len(self.__passanger_list_of_objects))

    def remove_alien(self, pass_obj):
        if not isinstance(pass_obj, Alien):
            raise TypeError('Aliens must be an instance of the Alien class')
        try:
            self.__passanger_list_of_objects.remove(pass_obj)
        except ValueError:
            raise ValueError(f'Инопланетянина {pass_obj.name} нет в списке пассажиров')

    def get_passanger_list(self):
        return self.__passanger_list_of_objects

    def set_seat_number(self, passanger):
        if not isinstance(passanger, str):
            raise TypeError('Чтобы обозначить номер сидения имя должно быть <str>')
        self.__seat_number = len(self.__passanger_list_of_objects)

class Bouncer:
    def main_function(self):
        return "Bounce"

o_alien_Pouk = Alien(name='Pouk')
print(vars(o_alien_Pouk))
for key, value in vars(o_alien_Pouk).items():
    print(f'{key}: {value}')

o_alien_Romness = Alien(name='Romness', color='Grey')

for key, value in vars(o_alien_Romness).items():
    print(f'{key}: {value}')

o_alien_seedling_Rebro = AlienSeedling(name='Rebro',color='orange')

for key, value in vars(o_alien_seedling_Rebro).items():
    print(f'atr<{key}>: {value}')

o_alien_seedling_Default = AlienSeedling()

for key, value in vars(o_alien_seedling_Default).items():
    print(f'atr<{key}>: {value}')

print('o_alien_seedling_Default.speed_mps = ', o_alien_seedling_Default.speed_mps)
o_alien_seedling_Default.alien_move(stand_and_stare=True)
print('o_alien_seedling_Default.speed_mps = ', o_alien_seedling_Default.speed_mps)

o_alien_seedling_Default.steal_human(1)
print(o_alien_seedling_Default.number_of_humans_stollen)

o_alien_seedling_Default.steal_human(10)
print(o_alien_seedling_Default.number_of_humans_stollen)
o_alien_seedling_Default.steal_human(1)

o_alien_Pouk.steal_human(1000)

print(o_alien_Pouk.number_of_humans_stollen)

print('o_alien_Pouk.__eye_color = ', o_alien_Pouk.get_alien_eye_color())
o_alien_Pouk.set_alien_eye_color('White')
print('o_alien_Pouk.__eye_color = ', o_alien_Pouk.get_alien_eye_color())

flying_Saucer_Pompom = Saucer(shape='Kiosk',saucer_flight_speed_mps=2000)

print(flying_Saucer_Pompom.flight_speed)

print(flying_Saucer_Pompom.get_passanger_list())

flying_Saucer_Pompom.add_alien(o_alien_Pouk)

print(flying_Saucer_Pompom.get_passanger_list())

flying_Saucer_Pompom.add_alien(o_alien_seedling_Default)

print(flying_Saucer_Pompom.get_passanger_list())

flying_Saucer_Pompom.remove_alien(o_alien_Pouk)

print(flying_Saucer_Pompom.get_passanger_list())

print(o_alien_seedling_Default.get_seat_number())

# o_alien_seedling_Default.set_seat_number(11)

print(o_alien_seedling_Default.get_seat_number())


print('+' * 100)

o_alien_seedling_lil_1 = AlienSeedling(name='Van Lav',color='pink')
o_alien_seedling_lil_2 = AlienSeedling(name='Too Kul',color='yellow')
o_alien_seedling_lil_3 = AlienSeedling(name='Free SpearIt',color='green')
o_alien_seedling_lil_4 = AlienSeedling(name='For Yu',color='blue')

o_scool_sauser = Saucer(shape='banana', saucer_flight_speed_mps=1500)

print(o_scool_sauser.get_passanger_list())
print(o_scool_sauser.saucer_shape)
print(o_scool_sauser.flight_speed)
o_scool_sauser.saucer_shape = 'Bug'
print(o_scool_sauser.saucer_shape)
o_scool_sauser.flight_speed = 1000
print(o_scool_sauser.flight_speed)
print(o_scool_sauser.get_passanger_list())


o_alien_Pouk.steal_human(12)

kek_bouncer = Bouncer

print(type(o_alien_seedling_lil_3))

o_scool_sauser.add_alien(o_alien_seedling_lil_1)
o_scool_sauser.add_alien(o_alien_seedling_lil_2)
o_scool_sauser.add_alien(o_alien_seedling_lil_3)
o_scool_sauser.add_alien(o_alien_seedling_lil_4)

print(o_scool_sauser.get_passanger_list())

print(o_alien_seedling_lil_4.get_seat_number())
print(o_alien_seedling_lil_3.get_seat_number())
print(o_alien_seedling_lil_2.get_seat_number())
print(o_alien_seedling_lil_1.get_seat_number())