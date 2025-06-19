var_int = 2
var_int = float(var_int)
#print(var_int)

#var_int = 'kekek'
#print(var_int)

var_float = 1.1

var_string = 'string'

result = var_int + var_float
# var_int_2 = var_int*15

#print(result, type(result))
#print(var_int, var_float, var_string)
#print(var_int_2)


var_list = list()
var_list = [1,2.33, 45, 'kek']
var_list2 = [1,2.33, 45, 'kek', var_list]
var_list3 = var_list + var_list2
#print(var_list)
#print(var_list2)
print(var_list3)

var_list3.append('privet')
print(var_list3)