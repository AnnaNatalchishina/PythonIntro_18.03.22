# # тип bool, None
# # приведение типов
# # оператор if
# # функция input
# # обработка ошибок
# ##################################################################
# none_value = None
# print(none_value, type(none_value))
#
# value = 123
# id_value = id(value)
# print(f"{id_value=}")
#
# print_value = print("---->", value)
# print(f"{print_value=}")
# ##################################################################
# value_1 = True
# value_2 = False
# print(type(value_1), type(value_2))
#
# bool_value = 21 != 21  # >, <, >=, <=, ==, !=
# bool_value = "we!" in "qwerty"
# print(bool_value)
# #################################################################
# value_int = 12
# value_float = 3.14
# result = value_float + value_int
# print(result)
#
# value_int = 10
# value_float = float(value_int)  # int -> float
# value_str = str(value_int)  # int -> str
# value_bool = bool(value_int)  # int -> bool  !!! True всегда, кроме 0
# print(value_str * 5, value_float, value_bool)
#
# ######################################################################
# value_float = -10.0
# value_int = int(value_float)  # float -> int   !!! "отрезание" всего после точки
# value_str = str(value_float)  # float -> str
# value_bool = bool(value_float)  # float -> bool  !!! True всегда, кроме 0.0
#
# print(value_int, value_str, value_bool)
# ######################################################################
# value_str = ""
# value_int = int(value_str)  # str -> int
# value_float = float(value_str)  # float -> str
# # утиная типизация
# value_bool = bool(value_str)  # float -> bool  !!! True всегда, кроме ""
# print(value_bool)
# print(value_bool, value_bool * 2)
#
# ############################### оператор if #########################
#
# value = 50
# # if условие:
# #     # блок, если ДА
# # elif условие_2:
# #     # блок, если ДА
# # else:
# #     # блок, если НЕТ
#
# if value > 100:
#     print(f"{value} больше чем 100")
# elif value < 100:
#     print(f"{value} меньше чем 100")
# else:
#     print(f"{value} равно 100")
#
# if value < 0:
#     print(f"{value} меньше чем 0")
# elif 0 <= value < 10:
#     print(f"{value}  больше 0 но меньше 10")
# elif 10 <= value < 100:
#     print(f"{value}  больше 10 но меньше 100")
# else:
#     print(f"{value} больше или равно 100")
#
#
# ######################## функция input ###############################
#
# input_value = input("Введи целое число: ")
# int_value = int(input_value)
# print(int_value * 2, type(int_value))
#
#
# int_value = int(input("Введи целое число: "))
# print(int_value * 2, type(int_value))
#
# ######################### обработка ошибок ########################
#
# input_value = input("Введи число с точкой: ")
# try:
#     int_value = float(input_value)
#     print(1 / int_value * 2)
# except ValueError:
#     print("Єто не целое число!")
# except ZeroDivisionError:
#     print("На 0 делить нельзя!!!!")
# except (ArithmeticError, AssertionError):
#     pass

######################################################################
#
# input_case = input("Вібери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
# value_1 = input("Введи первое число:")
# value_2 = input("Введи второе число:")
# if input_case == '1':
#     result = value_1 + value_2
# print(result)

www = "www.conquer_and_command.net"

if ".com" in www:

    print("com in www")

else:

    print("com not in www")




