# tuple - кортеж, list - список

my_tuple = (1, 2, 3, "qwerty", True, None)    # не изменяемый объект
my_list = [1, 2, 3, "qwerty", True, None] # изменяемый объект
# print(type(me_tuple), type(my_list))


######################## итерируемые объекты

# print(my_list[20:])

# new_tuple = tuple(my_list)
# print(new_tuple)
#
# new_list = list(my_tuple)
# print(new_list)


##########################

# new_list = list()
# print(new_list)
#
# new_tuple = tuple()

# my_new_list = [10, 12] * 4
#
# print(my_new_list)

# base_list = [1, 2, 3]
# new_list = [base_list] * 5
# print(new_list)

#################################
my_tuple = (1, 2, 3, "qwerty", True, None, ['tuple'])    # не изменяемый объект
my_list = [1, 2, 3, "qwerty", True, None, 'list'] # изменяемый объект

# value = "10"
# my_list[0]= value
# print(my_list)

# value = "10"
# my_tuple[-1][0] = value
# print(my_tuple)
#
# my_list = [1, 2, 3]
# index_value = 4
# value = 100
# if len(my_list) > index_value:

# try:
#     value = my_list [index_value]
#     print(value)
# except IndexError:
#     pass
# print(value)



##############################################


# my_list = []
#
# my_list.append(100) # добавляем элемент в конец списка
# print(my_list)

# my_list = []
# my_str = "qwerty"
# # my_list.append(100) # добавляем элемент в конец списка
# for symbol in my_str:
#     my_list.append(symbol)
# # my_list = list(my_str)
# print(my_list)

######################################

# my_str = "qwerty"
# my_list = list(my_str)
# print(my_list)
# new_str = "". join(my_list)
# print(new_str)

# my_str = "qwerty"
# my_list = list(my_str)
# print(my_list)
# new_str = "...". join(my_list)
# print(new_str)

# my_list = ["tmp", "home", "images"]
# new_str = "/".join(my_list)
# print(new_str)

#
# file_path = "/home/zva/PycharmProjects/PythonIntro_14_03_22/6.py"
# parts = file_path.split("/")
# print(parts)
# parts[-1] = "text.txt"
# file_path = "/".join(parts)
# print(file_path)


######################### сортировка


