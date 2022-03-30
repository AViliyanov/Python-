from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(el, el_1):
    return el * el_1

print(reduce(my_func,my_list))
