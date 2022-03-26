def my_func(num_1, num_2, num_3):
    try:
        res_1 = int(num_1) + int(num_2)
        res_2 = int(num_2) + int(num_3)
        res_3 = int(num_1) + int(num_3)
        return max(res_1, res_2, res_3)
    except ValueError as err:
        return err


print(my_func(input("Num_1:"), input("Num_2:"), input("num_3:")))
