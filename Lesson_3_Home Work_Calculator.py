
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







