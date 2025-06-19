import datetime

class Human():
    def __init__(self, name='Mihail',surname='Smirnov',age='39'):
        self.human_body = 1
        self.name = name
        self.surname = surname
        self.age = age
        self.rota = None
        self.polk = None

        age_int_days = int(self.age) * 365.25
        full_years_age_datetime = datetime.timedelta(days=age_int_days)
        time_utc_now = datetime.datetime.now(datetime.timezone.utc)
        self.time_of_birth = time_utc_now - full_years_age_datetime

    def set_rota(self, new_rota):
        self.rota = new_rota

    def set_polk(self, new_polk):
        self.polk = new_polk

    def __repr__(self):
        return f'Human({self.name} {self.surname}, Age: {self.age})'

    def get_info(self):
        return f'{self.name} {self.surname}, {self.age} лет'