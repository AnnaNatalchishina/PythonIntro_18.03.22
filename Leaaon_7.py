# my_str = "blablacar"
# my_symbol = "bla"
#
# result = my_str.count(my_symbol)
# print(result)
#
# count = my_str.count(my_symbol)
# for _ in range(count):
#     print(my_symbol)

# my_str = "bla BLA car"

my_str = "jhdjahihjkljkl, jkljlkjlk"
my_list = []
for index, symbol in enumerate(my_str):
    if not index % 2:
        my_list.append(symbol)
print(my_list, id(my_list))
