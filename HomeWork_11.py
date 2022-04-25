import os

# Все пункты являются частью одного задания, поэтому можно использовать функции несколько раз и не дублировать код.
# Если хотите, можете использовать значения по умолчанию и аннотацию типов.
#
# 1. Написать функцию, которая получает один параметр - имя директории и возвращает словарь вида
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#



name_dir = "Directory_1"

def get_dir (name_dir):
    dic = {'filenames': [], 'dirnames': []}
    list_dir_and_file = os.listdir(name_dir)
    for value in list_dir_and_file:
        path = os.path.join(name_dir, value)
        if os.path.isdir(path):
            dic['dirnames'].append(value)
        elif os.path.isfile(path):
            dic['filenames'].append(value)
    return dic

dict_dir_and_file = get_dir(name_dir)
print(dict_dir_and_file)


# 2. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1
# и булевое значение (True/False) - можно сделать параметром по умолчанию.
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#


sort_alphabet = False

def sort_dir (dict_name, sort_parametr):
    dict_name['filenames'].sort(reverse=not sort_parametr)
    dict_name['dirnames'].sort(reverse=not sort_parametr)
    return dict_name


sort_dict = sort_dir(dict_dir_and_file, sort_alphabet)
print(sort_dict)

# 3. Написать функцию, которая получает два параметра - словарь, описанный в пункте 1 и строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.

name_str = "Filename.txt"

def add_dict_str (dic, name_string):
    if '.' in name_string:
        dic['filenames'].append(name_string)
    else:
        dic['dirnames'].append(name_string)
    return dic


new_dict = add_dict_str(dict_dir_and_file, name_str)
print(new_dict)