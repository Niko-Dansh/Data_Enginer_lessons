import datetime

current_time_utc = datetime.datetime.now(datetime.timezone.utc)

print(current_time_utc)

minus_one_hour = datetime.timedelta(hours=1)

print(minus_one_hour)

one_hour_ago_time = current_time_utc - minus_one_hour

print(one_hour_ago_time)

print('-' * 100)

import pandas as pd
from Utils2.Human import Human

o_human_from_import_1 = Human()

print(o_human_from_import_1.get_info())

print('-' * 100)

#Human additional functions

from Utils2.Rota import Rota
from Utils2.Polk import Polk

o_human_import_test_1 = Human(name='Human_Test_1')
o_human_import_test_2 = Human(name='Human_Test_2')
o_human_import_test_3 = Human(name='Human_Test_3')
o_human_import_test_4 = Human(name='Human_Test_4')

o_rota_import_test_1 = Rota(rota_name='Rota_test_1')
o_rota_import_test_2 = Rota(rota_name='Rota_test_2')

o_polk_import_test_1 = Polk(polk_name='Polk_test_1')

o_polk_import_test_1.add_rota(o_rota_import_test_1)
o_polk_import_test_1.add_rota(o_rota_import_test_2)

o_rota_import_test_1.add_soldier(o_human_import_test_1)
o_rota_import_test_1.add_soldier(o_human_import_test_2)

o_rota_import_test_2.add_soldier(o_human_import_test_3)
o_rota_import_test_2.add_soldier(o_human_import_test_4)


def add_human_to_rota(added_human_list: list, rota_to_add: Rota):
    for item in added_human_list:
        item.set_rota(rota_to_add)
        item.set_polk(rota_to_add.polk)
        rota_to_add.add_soldier(item)


o_human_import_test_5 = Human(name='Human_Test_5')

print(o_rota_import_test_1.soldiers_list)
add_human_to_rota(added_human_list=[o_human_import_test_5], rota_to_add=o_rota_import_test_1)
print(o_rota_import_test_1.soldiers_list)
print(o_human_import_test_5.rota, o_human_import_test_5.polk)

print(o_polk_import_test_1.get_all_soldiers())

print('-' * 100)

def add_rotas_to_polk(rotas_to_add: list, to_which_polk: Polk):
    for rota in rotas_to_add:
        to_which_polk.add_rota(rota)
        for soldier in rota.get_soldiers_info():
            soldier.set_polk(to_which_polk)

o_rota_import_test_3 = Rota(rota_name='Rota_3_Filled',rota_dislocation='Balashiha')
print(o_rota_import_test_3.polk)
print(o_rota_import_test_3.soldiers_list)
o_human_import_test_10 = Human(name='Human_Test_10')
o_human_import_test_11 = Human(name='Human_Test_11')
print('-' * 100)
print(o_human_import_test_10.rota)
print(o_human_import_test_10.polk)
print(o_human_import_test_11.rota)
print(o_human_import_test_11.polk)
print('-' * 100)
add_human_to_rota(added_human_list=[o_human_import_test_10, o_human_import_test_11], rota_to_add=o_rota_import_test_3)

print(o_rota_import_test_3.polk)
print(o_rota_import_test_3.soldiers_list)
print('-' * 100)
print(o_human_import_test_10.rota)
print(o_human_import_test_10.polk)
print(o_human_import_test_11.rota)
print(o_human_import_test_11.polk)
print('-' * 100)

add_rotas_to_polk(rotas_to_add=[o_rota_import_test_3], to_which_polk=o_polk_import_test_1)

print('Rota 3/ Polk: ', o_rota_import_test_3.polk)
print('Rota 3/ soldiers_list: ', o_rota_import_test_3.soldiers_list)
print('Human 10/ rota: ', o_human_import_test_10.rota)
print('Human 10/ polk: ', o_human_import_test_10.polk)
print('Human 11/ rota: ', o_human_import_test_11.rota)
print('Human 11/ Polk: ', o_human_import_test_11.polk)

print('-' * 100)

print('Human 1/ time_of_birth : ', o_human_import_test_1.time_of_birth)
print('Human 2/ time_of_birth : ', o_human_import_test_2.time_of_birth)
print('Human 3/ time_of_birth : ', o_human_import_test_3.time_of_birth)
print('Human 4/ time_of_birth : ', o_human_import_test_4.time_of_birth)
print('Human 5/ time_of_birth : ', o_human_import_test_5.time_of_birth)
print('Human 10/ time_of_birth : ', o_human_import_test_10.time_of_birth)
print('Human 11/ time_of_birth : ', o_human_import_test_11.time_of_birth)

