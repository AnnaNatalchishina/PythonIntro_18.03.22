# Ctrl + ? - закоментировать строку
# переменная

value = 3
new_value = 5.1  # new_type
my_str = "Hello!!!"

print(value, new_value, my_str, print)

# type() - функция получения типа обекта
# int - тип цельіх чисел <class 'int'>
print(type(value))

val_1 = 9
val_2 = 2
result = val_1 + val_2
result = val_1 * val_2
result = val_1 - val_2
result = val_1 / val_2
result = val_1 // val_2  # целочисленное деление (целая часть числа в МАТЕМАТИЧЕСКОМ смисле)
result = val_1 % val_2  # остаток от деления (в МАТЕМАТИЧЕСКОМ смисле)
# my_new_vali_ue_jSgfasjdjszg_yjszcg_dghsjdhbcmzxhbcmqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq_1 = 3  # НЕ ДЕЛАЙ ТАК!!!
result = val_1 ** val_2
print(result, type(result))
###############################################################
val_1 = 30.9
val_2 = 10.4
result = val_1 + val_2
result = val_1 * val_2
result = val_1 - val_2
result = val_1 / val_2
result = val_1 // val_2  # целочисленное деление есть, но не рекомендую
result = val_1 % val_2  # остаток от деления есть, но не рекомендую
print(result, type(result))
###################################################################
value_int = 3
value_float = 4.3
value_int = value_float
value_float = 5
# id() - функция получения id обекта
print(id(value_int), id(value_float))
###################################################################
a, b = 2, 4
a, b = b, a
print(a)
###################################################################
my_str = "New_string"
my_str = 'New_string'
my_str = """New_string"""
my_str = '''New_string'''
my_str = 'FC "Arsenal"'
my_str = "I'm a boy"
print(my_str, type(my_str))
new_str = r'My\tname\tis\nVova'  # raw string

f_str = f'My value is {value}'
f_str = f"{value=}"
print(f_str)
###################################################################
my_int = 1
my_float = 3.14
my_str = "i"
new_str = "ing"
result = my_str * 10
print(result)
###################################################################
folder = "images"
filename = "photo_1"
ext = "png"
path = folder + "/" + filename
path = "{}/{}.{}".format(folder, filename, ext)
path = f"{folder}/{filename}.{ext}"
print(path)

# PEP8 formatting: Ctrl + Alt + l    !!!!!!!!!!!!!!!!!!!!!!!!!