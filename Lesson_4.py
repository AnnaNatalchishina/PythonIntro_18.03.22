# or, and, not
# while
# str

############### while ###############

# value = 10
#
# while value > 0:
#     print(value)
#     # value = value - 1 # valie -= 1 - уменьшение на 1
#     value -=1


# while True:
#     print(value)
#     value -= 1
#     if value <= 0:
#         break


# or, and, not
coffee = False
tea = False

# result = coffee or tea
# print(result)
# value = not coffee
# print(value)

# value = 15
#
# if not value % 2 == 0 and not value % == 0: # if value == True - плохая практика if value == True: хорошая практика
#     print(f"{value} делится на 6")

# value = "*"
#
# if value == "*" or

# or-или, and-и, not-не
# while
# тернарный оператор
# str

# my_str = "qwertyas,jdhfgjasbvdfasvghmdfwavhmsdv cnzsvdfhmsvzdcn zxvdhmcawfsdbcv ZNm vjnzdkgvcAZCFXvbxzm,jvn.exe"
# index = 120
# symbol = my_str[index]
# print(symbol)
# if index < len(my_str):
#     print(my_str[index])
#
# # срез
# my_str = "qwerty"
# result = my_str[2:5]  # срез [старт:финиш(не включен):шаг]
# result = my_str[1:]
# result = my_str[:-1]
# result = my_str[:]  # копия строки
# result = my_str[-30:]
# result = my_str[1:5:2]
# result = my_str[::-1]  # - разворот строки
# result = my_str[::2]  # - на четных индексах(местах)
# result = my_str[1::2]  # - на нечетных индексах(местах)
# print(result)
#
#
# value = -123
# my_str = str(value) if value > 0 else str(value)[::-1]
# print(my_str)
#
# ############################################################################################################
#
# number = 100
#
# # if number >= 0:
# #     result = number ** 0.5
# # else:
# #     result = -1
#
# result = number ** 0.5 if number >= 0 else -1
# print(result)
#
# ############################################################################################################
# value = 10
#
# while value > 0:
#     print(value)
#     # value = value - 1  тоже что и value -= 1 - уменьшение на 1
#     value -= 1
#
# while True:
#     print(value)
#     value -= 1
#     if value <= 0:
#         break
#
# go_loop = True
# while go_loop:
#     print(value)
#     value -= 1
#     if value <= 0:
#         go_loop = False
#
#
#
#
#
# ############################################################################################################
# # or-или, and-и, not-не
# coffee = False
# tea = True
# water = False
#
# result = coffee or (tea and water)
#
# result = coffee or tea
# print(result)
# value = not coffee
# print(value)
#
# value = 12
#
# if value % 2 == 0 and value % 3 == 0:  # if value == True: - плохая практика, if value: - хорошая практика
#     print(f"{value} делится на 6")
#
# if not value % 2 and not value % 3:
#     print(f"{value} делится на 6")
#
# value = "qwe"
#
# if value in "* + - / **":
#     print("!!!")
# else:
#     print("???")


    ##################################################

# or-или, and-и, not-не
# while
# тернарный оператор
# str

my_str = "qwertyas,jdhfgjasbvdfasvghmdfwavhmsdv cnzsvdfhmsvzdcn zxvdhmcawfsdbcv ZNm vjnzdkgvcAZCFXvbxzm,jvn.exe"
index = 120
symbol = my_str[index]
print(symbol)
if index < len(my_str):
    print(my_str[index])

# срез
my_str = "qwerty"
result = my_str[2:5]  # срез [старт:финиш(не включен):шаг]
result = my_str[1:]
result = my_str[:-1]
result = my_str[:]  # копия строки
result = my_str[-30:]
result = my_str[1:5:2]
result = my_str[::-1]  # - разворот строки
result = my_str[::2]  # - на четных индексах(местах)
result = my_str[1::2]  # - на нечетных индексах(местах)
print(result)


value = -123
my_str = str(value) if value > 0 else str(value)[::-1]
print(my_str)

############################################################################################################

number = 100

# if number >= 0:
#     result = number ** 0.5
# else:
#     result = -1

result = number ** 0.5 if number >= 0 else -1
print(result)

############################################################################################################
value = 10

while value > 0:
    print(value)
    # value = value - 1  тоже что и value -= 1 - уменьшение на 1
    value -= 1

while True:
    print(value)
    value -= 1
    if value <= 0:
        break

go_loop = True
while go_loop:
    print(value)
    value -= 1
    if value <= 0:
        go_loop = False





############################################################################################################
# or-или, and-и, not-не
coffee = False
tea = True
water = False

result = coffee or (tea and water)

result = coffee or tea
print(result)
value = not coffee
print(value)

value = 12

if value % 2 == 0 and value % 3 == 0:  # if value == True: - плохая практика, if value: - хорошая практика
    print(f"{value} делится на 6")

if not value % 2 and not value % 3:
    print(f"{value} делится на 6")

value = "qwe"

if value in "* + - / **":
    print("!!!")
else:
    print("???")