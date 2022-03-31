
# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
#
value = 20
new_value = value / 2 if value <100 else -value
print(new_value)

# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
#
value = 500
new_value = 1 if value <100 else 0
print(new_value)

# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False
#
value = 200
new_value = True if value <100 else False
print(new_value)

# 4) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
#
my_str = "qwer"
if len(my_str)<5:
    result = my_str + my_str
else:
    result = my_str
print(result)

# 5) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
#
my_str = "qwer"
if len(my_str)<5:
    result = my_str + my_str[::-1]
else:
    result = my_str
print(result)

# 6) Доработать задание с калькулятором, чтобы в конце вычисления у пользователя спрашивало, нужен ли калькулятор еще.
# И если да, то запустить вычисление заново

value = "y"
while value == "y":

    input_case = input("Выбери тип операции: \n1 +\n2 -\n3 *\n4 /\n")

    try:
        input_value_int = int(input_case)
        value_1 = input("Введите первое число:")
        value_2 = input("Введите второе число:")

        value_float_1 = float(value_1)
        value_float_2 = float(value_2)

        if input_case == "1":

            result = value_float_1 + value_float_2
            print(result)

        elif input_case == "2":

            result = value_float_1 - value_float_2
            print(result)

        elif input_case == "3":

            result = value_float_1 * value_float_2
            print(result)

        elif input_case == "4":

            result = value_float_1 / value_float_2
            print(result)

    except ValueError:
        print("Это не число!")

    except ZeroDivisionError:
        print("На 0 делить нельзя!")

    value = input("Нужен ли калькулятор еще?\nЕсли да - введи 'y', если нет - введи любое значение: ")
