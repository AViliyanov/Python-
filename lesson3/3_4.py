def my_func(x, z):
    res = abs(x) ** -abs(z)
    return res


print(my_func(float(input("x:")), int(input("z:"))))
