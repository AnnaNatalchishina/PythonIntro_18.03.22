# 1. Инициализация класса с одним параметром - имя директории.
#
# 2. Написать метод экземпляра класса, который создает атрибут экземпляра класса в ввиде словаря
# {'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
# Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
#
# 2. Написать метод экземпляра класса, которая получает булевое значение (True/False).
# Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
# Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.
#
# 3. Написать метод экземпляра класса, которая получает строку, которая может быть
# или именем файла, или именем папки. (В имени файла должна быть точка).
# В зависимости от того, что функция получила (имя файла или имя папки) - записать его в соответствующий список
# и вернуть обновленный словарь.

import os


class Check_folder_files:
    def __init__(self, dirname, sort_alphabet, name_string):
        self.dirname = dirname
        self.dic = self.get_dir()
        self.sort_alphabet = sort_alphabet
        self.name_string = name_string

    def get_dir(self):
        dic = {'filenames': [], 'dirnames': []}
        list_dir_and_file = os.listdir(self.dirname)
        for value in list_dir_and_file:
            path = os.path.join(self.dirname, value)
            if os.path.isdir(path):
                dic['dirnames'].append(value)
            elif os.path.isfile(path):
                dic['filenames'].append(value)
        return dic

    def sort_dir(self):
        self.dic['filenames'].sort(reverse=not self.sort_alphabet)
        self.dic['dirnames'].sort(reverse=not self.sort_alphabet)

    def add_dict_str(self):
        if '.' in self.name_string:
            self.dic['filenames'].append(self.name_string)
        else:
            self.dic['dirnames'].append(self.name_string)

name_dir = "Directory_1"
sort_alphabet = False
name_str = "Filename.txt"

worker = Check_folder_files(name_dir, sort_alphabet, name_str)
print(worker.dic)
worker.sort_dir()
print(worker.dic)
worker.add_dict_str()
print(worker.dic)




