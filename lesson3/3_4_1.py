def my_func(x, z):
    for i in range(1, z-1):
        x *= x
    res = 1 / x
    return res


print(my_func(float(input("x:")), int(input("z:"))))
