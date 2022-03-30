
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list = [v for el, v in enumerate(my_list) if my_list[el] > my_list[el - 1] and el != 0]


print(list)
