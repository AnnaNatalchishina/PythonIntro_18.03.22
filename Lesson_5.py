# debuger
# for
# str methods


my_str = "My name is Anna, i'm 40. It is dog."

my_str_len = len(my_str)
print(my_str_len)
print(my_str.isupper())

for symbol in my_str:
    if not symbol.isupper():
        print(symbol)

result = ""
for symbol in my_str:
    if symbol.isalpha() and symbol.islower() and symbol not in 'eyuioa':
        result += symbol
print(result)

result = my_str.rfind("m")
print(result)


filename = "image_png_123.png"
f_name = filename[::-1].replace("gnp", "gpj", 1)
filename = f_name[::-1]
# filename = filename.replace('png', 'jpg', 1)
print(filename)

for symbol in my_str:
    if symbol.lower() in 'eyuioa':
        print(symbol)

print(my_str.lower().count('a'))


######################################################################

my_str = "qwerty123456"

for symbol in my_str:
    print(symbol)

for symbol in my_str[:6]:
    print(symbol)


for index in range(len(my_str)):
    print(index, my_str[index])


for index, symbol in enumerate(my_str):
    print(index, symbol)

for item in enumerate(my_str):
    print(item)


######################## разбор ДЗ калькулятор #######################
input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n: ")

if input_case in "1234":
    try:
        value_1 = float(input("Ведите первое число:"))
        value_2 = float(input("Ведите второе число:"))
        if input_case == "1":
            result = value_1 + value_2
            sign = '+'
        elif input_case == "2":
            result = value_1 - value_2
            sign = '-'
        elif input_case == "3":
            result = value_1 * value_2
            sign = '*'
        else:
            result = value_1 / value_2
            sign = '/'
        print(f'{value_1} {sign} {value_2} = {result}')
    except ZeroDivisionError:
        print("На ноль делить нельзя, повторите еще раз")
    except ValueError:
        print("Это не число, попробуйте еще раз")
else:
    print("Вы не выбрали операцию, повторите еще раз")