# Все пункты сделать как отдельные функции и их вызовы.
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
#

filename = "domains.txt"


def get_domains(filename):
    with open(filename, "r") as my_file:
        data = my_file.read()

    my_list = []
    for domain in data.split("\n"):
        my_list.append(domain[1:])
    return my_list


list_domains = get_domains(filename)
print(list_domains)

# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"
#
#
filename = "names.txt"


def create_names(filename):
    with open(filename, "r") as mine_file:
        data = mine_file.read()

    my_list = []
    for data_line in data.split("\n"):
        name = data_line.split('\t')[1]
        my_list.append(name)
    return my_list


list_names = create_names(filename)
print(list_names)

# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date": date}
# в которых date - это дата из строки (если есть),
# Например [{"date": "1st January 1919", "date": "8th February 1828"},  ...]
#

# filename = "authors.txt"
#
#
# def get_dates(filename):
#     with open(filename, "r") as file_:
#         data = file_.read()
#     my_list = []
#     for line in data.split("\n"):
#         for value in line.split():
#             if value.isdigit():
#                 date = line[:line.find('-')]
#                 my_list.append({'date': date})
#     return my_list
#
#
# dates = get_dates(filename)
# print(dates)


filename = "authors.txt"


def get_dates(filename):
    with open(filename, "r") as file_:
        data = file_.read()
    my_list = []
    for line in data.split("\n"):
        if " - " in line:
            date = line[:line.find(' -')]
            my_list.append({'date': date})
    return my_list


dates = get_dates(filename)
print(dates)
