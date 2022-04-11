# 1. Дано целое число (int). Определить сколько нулей в этом числе.
#
# my_int = 10000
# my_str = str(my_int)
# my_symbol = "0"
# count = my_str.count(my_symbol)
# print(count)


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
#
# my_int = 10020000
# my_list = list(str(my_int)[::-1])
# counter = 0
# while my_list[0] == '0':
#     counter += 1
#     my_list.pop(0)
#
# print(counter)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#

# my_list_1 = ['q', 6, 'w', 8, 't']
# my_list_2 = ['a', 9, 'u', 10]
# my_result = []
# my_result = my_list_1[::2] + my_list_2[1::2]
#
# print(my_result)


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
#
# my_list = [1, 2, 3, 4, 5, 6]
# new_list = my_list[1:]
# new_list.append(my_list[0])
# print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = [1, 2, 3, 4, 5, 6]
# symbol = my_list.pop(0)
# my_list.append(symbol)
# print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#
# my_str = "40 > чем 30 < чем 50"
# my_list = my_str.split()
# result = 0
#
# for symbol in my_list:
#     if symbol.isdigit():
#         result += int(symbol)
# print(result)




# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
#

# my_str = "My long string"
# l_limit = "l"
# r_limit = "i"
# sub_str = my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit)]
# print(sub_str)

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
#
# my_str = 'qwertyu'
# my_list = []
#
# if len(my_str) %2 != 0:
#     my_str += "_"
# for i in range(0, len(my_str), 2):
#     my_list.append(my_str[i:i+2])
# print(my_list)





# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
#
# my_list = [1, 20, 3, 4, 5, 9, 1]
# counter = 0
#
# for i in range(1, len(my_list) - 1):
#     if my_list[i] > my_list[i - 1] + my_list[i + 1]:
#         counter += 1
#
# print(counter)


# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
#
# my_list = [3, 7, 9, "15", 50, "32"]
# new_list = []
# for symbol in my_list:
#     if type(symbol) == str:
#         new_list.append(symbol)
# print(new_list)



# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
#
# my_str = "qwertyqweqweqweqweqweqweqwwewqwewqwqwqw"
# my_list = []
# my_set = set(my_str)
# for symbol in my_set:
#     if my_str.count(symbol) == 1:
#         my_list.append(symbol)
# print(my_list)


# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
#
# str_1 = "qwe"
# str_2 = "qwertyvbnm"
# my_list = list(set(str_1).intersection(set(str_2)))
# print(my_list)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

# str_1 = "qwerttyuui"
# str_2 = "qweertyy"
# my_list = []
# my_set = set(str_1).intersection(set(str_2))
#
# for symbol in my_set:
#     if str_1.count(symbol) == 1 and str_2.count(symbol) == 1:
#         my_list.append(symbol)
#
# print(my_list)