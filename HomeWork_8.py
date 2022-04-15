# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
#

my_list = ["qwerty", 'tr6', '7p', "54"]
new_list = []
for index, value in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(value)
    else:
        new_list.append(value[::-1])
print(new_list)



# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
#
my_list = ["qwertya", 'atr6', '7pa', "a54"]
new_list = []
for value in my_list:
    if value[0] == "a":
        new_list.append(value)
print(new_list)



# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#
my_list = ["qwertya", 'atr6', '7pa', "a54"]
new_list = []
for value in my_list:
    if 'a' in value:
        new_list.append(value)
print(new_list)




# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.
#

persons = [{"name": "John", "age": 15},
           {"name": "Alice", "age": 6},
           {"name": "Jack", "age": 45}]
# a)
list_result_a = []
min_age = []
for dic in persons:
    min_age.append(dic["age"])

for dic in persons:
    if dic["age"] == min(min_age):
        list_result_a.append(dic["name"])

print(list_result_a)

# б)

list_result_b = []
max_name = []
for dic in persons:
    max_name.append(len(dic["name"]))

for dic in persons:
    if len(dic["name"]) == max(max_name):
        list_result_b.append(dic["name"])

print(list_result_b)

# в)

ages = []
for person in persons:
    ages.append(person["age"])
average_age = sum(ages) / len(ages)

print(average_age)




# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# a)
my_dict_1 = {"name": "John", "age": 15, 5: "2"}
my_dict_2 = {"name": "Alice", "age": 6, "5": 2}

my_list = []
set_dict_1 = set(my_dict_1.keys())
set_dict_2 = set(my_dict_2.keys())
my_list = list(set_dict_1.intersection(set_dict_2))

print(my_list)

# б)
my_list = []
set_dict_1 = set(my_dict_1.keys())
set_dict_2 = set(my_dict_2.keys())
my_list = list(set_dict_1.difference(set_dict_2))
print(my_list)

# в)
new_dict = {}
set_dict_1 = set(my_dict_1.keys())
set_dict_2 = set(my_dict_2.keys())
set_difference = set_dict_1.difference(set_dict_2)

for key in set_difference:
    new_dict[key] = my_dict_1[key]

print(new_dict)

# г)
new_dict = {}
set_dict_1 = set(my_dict_1.keys())
set_dict_2 = set(my_dict_2.keys())
list_union_key = list(set_dict_1.union(set_dict_2))
for key in list_union_key:
    if key in my_dict_1.keys() and key in my_dict_2.keys():
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
    elif key in my_dict_1.keys():
        new_dict[key] = my_dict_1[key]
    else:
        new_dict[key] = my_dict_2[key]

print(new_dict)