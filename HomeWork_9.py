import string
import random

# Для задания 1-7 за основу можете взять код из предідущих ДЗ.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
#
my_list = ["qwertya", 'atr6', '7p', "a54"]


def get_new_list(list_str):
    new_list = []
    for index, value in enumerate(list_str):
        if index % 2 == 0:
            new_list.append(value)
        else:
            new_list.append(value[::-1])
    return new_list


print(get_new_list(my_list))


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".
#


def create_list_str_a(list_str):
    new_list = []
    for value in list_str:
        if value[0] == "a":
            new_list.append(value)
    return new_list


print(create_list_str_a(my_list))


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.
#


def create_list_str_with_a(list_str):
    new_list = []
    for value in list_str:
        if 'a' in value:
            new_list.append(value)
    return new_list


print(create_list_str_with_a(my_list))

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.
#
my_list_type = [3, 7, 9, "qwertya", 'atr6', '7pa', "a54"]


def create_str(list_):
    new_list = []
    for symbol in list_:
        if type(symbol) == str:
            new_list.append(symbol)
    return new_list


print(create_str(my_list_type))

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.
#

my_str = "qwertyqweqweqweqweqweqweqwwewqwewqwqwqw"


def create_one(str_):
    list_value = []
    my_set = set(str_)
    for symbol in my_set:
        if str_.count(symbol) == 1:
            list_value.append(symbol)
    return list_value


print(create_one(my_str))

# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#

str_1 = "qwerttyuui"
str_2 = "qweeryy"


def create_at_least_once(str_one, str_two):
    list_result = list(set(str_one).intersection(set(str_two)))
    return list_result


print(create_at_least_once(str_1, str_2))


# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


def create_once(str_one, str_two):
    list_result = []
    my_set = set(str_one).intersection(set(str_two))
    for symbol in my_set:
        if str_one.count(symbol) == 1 and str_two.count(symbol) == 1:
            list_result.append(symbol)
    return list_result


print(create_once(str_1, str_2))

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com

names = ["jones", "ford", "sheeran"]
domains = ["net", "com", "ua"]


def create_email(domains_list, names_list):
    number = random.randint(100, 999)
    alphabet = string.ascii_lowercase
    rand_name = ''
    for _ in range(0, random.randint(5, 7)):
        rand_name += random.choice(alphabet)
    e_mail_name = f'{random.choice(names_list)}.{number}@{rand_name}.{random.choice(domains_list)}'
    return e_mail_name


e_mail = create_email(domains, names)
print(e_mail)
