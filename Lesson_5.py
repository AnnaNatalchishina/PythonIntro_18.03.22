####### for ####


# my_str = "My name is John"

# my_str_len = len(my_str)
# print(my_str_len)

# print(my_str.isalpha())
# for symbol in my_str:
#     if symbol.isupper():
#         print(symbol)


# for symbol in my_str:
#     if symbol not in 'eyuio':
#         print(symbol)

# result = my_str.find("John")
# print(result)

# filename = "image_123.png"
# filename.replace('png', 'jpg')
# print(filename)

# my_str = "My name is Anna, i'm 40. It is a dog"
# #
# # for symbol in my_str:
# #     if symbol.lower() in 'eyuioa':
# #         print(symbol)
#
# print(my_str.count('Anna'))


#################################
# for symbol in my_str:
#     print(symbol)
#
# my_str = "qwerty1234456"
#
# for symbol in my_str[:6]:
#     print(symbol)
#
# for index in range(len(my_str)):
#     print(index, my_str[index])
#
# for index, symbol in enumerate(my_str):
#     print(index, symbol)


my_str = "My name is Vova. I am a teacher !"



for symbol in my_str:

    if symbol.isupper() and symbol not in 'EYUIOA':

        print(symbol)