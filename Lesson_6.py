# tuple - кортеж, list - список

my_tuple = (1, 2, 3, "qwerty", True, None, 'tuple')  # неизменяемый объект
my_list = [1, 2, 3, "qwerty", True, None, 'list']  # изменяемый объект
print(type(my_tuple), type(my_list))

########### итерируемые объекты
print(my_list[:20])

new_tuple = tuple(my_list)
print(new_tuple)

new_list = list(my_tuple)
print(new_list)
############################################
new_list = list()
print(new_list)

new_tuple = tuple()
print(new_tuple)

new_list = list("qwerty")
new_list = ["qwerty", ]
print(new_list, type(new_list))

new_tuple = tuple("qwerty")
new_tuple = ("qwerty",)
print(new_tuple, type(new_tuple))

new_list = ["12.240.12.1",
            "12.240.12.12",
            "12.240.12.112",
            "123.255.12.01",
            "123.255.12.02",
            "123.255.12.03",
            ]

base_list = [1, 2, 3]
my_new_list = base_list * 4
print(my_new_list)
base_list[0] = 10
print(f"{base_list=}")
print(f"{my_new_list=}")

######################################
base_list = [1, 2, 3]  #  <<<<<<<<<<<<<<<<<<<<<<<<<<<<
new_list = [base_list.copy()] * 3
print(new_list)
base_list[0] = 10
print(f"{base_list=}")
print(f"{new_list=}")
######################################
my_tuple = (1, 2, 3, "qwerty", True, None, ['tuple'])  # неизменяемый объект
my_list = [1, 2, 3, "qwerty", True, None, ('list', )]  # изменяемый объект

# value = "10"
# my_list[-1][0] = value
# print(my_list)

value = "10"
my_list[-1] = (value, )
print(my_list)
##################################################################
my_list = [1, 3]
if my_list:
    value = my_list[0]
    print(value)

my_list = [1, 2, 3]
index_value = 4
value = 100
if len(my_list) > index_value:
    value = my_list[index_value]

# try:
#     value = my_list[index_value]
# except IndexError:
#     pass
# print(value)
#############################################################
my_list = []
my_str = "qwerty"
# my_list.append(100)  # добавляем элемент в конец списка
for symbol in my_str:
    my_list.append(symbol)
# my_list = list(my_str)
print(my_list)

del_value = my_list.pop()
print(my_list, del_value)
##############################################################
my_str = "qwerty"
my_list = list(my_str)
print(my_list)
new_str = "".join(my_list)
print(new_str)
my_list = ["tmp", "home", "images", "photo.png"]
new_str = "/".join(my_list)
print(new_str)

file_path = "home/zva/PycharmProjects/PythonIntro_14_03_22/lesson_6.py"
parts = file_path.rsplit("/", 1)
print(parts)
parts[-1] = "test.txt"
file_path = "/".join(parts)
print(file_path)

parts = file_path.rsplit("lesson_")
print(parts)
########################### сортировка
# my_list = [2, 5, 1, 9, -4, 7]
my_list = ["tmp", "amp", "aamp", "home", "Images", "photo.png", "123", "@", "["]

# my_list.sort()  # сортирует текущий список без возможности вернуть старый порядок
# print(my_list)
sort_list = sorted(my_list, key=len, reverse=True)  # сортирует копию списока
print(sort_list)

# ASCII - таблица символов

print(ord("a"), ord("1"), ord("@"), ord("I"), ord("["))
print(chr(102))


