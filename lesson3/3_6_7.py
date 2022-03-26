def int_func(*args):
    global v

    for i, v in enumerate(args):
        i = str(v)
    return v.title()


print(int_func(input("Text:")))
