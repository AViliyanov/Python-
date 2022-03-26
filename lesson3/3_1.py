def argument(del_1, del_2):
    try:
        res = int(del_1) / int(del_2)
        return res
    except (ZeroDivisionError, ValueError) as err:
        return err


print(argument(input("Number_1:"), input("Number_2:")))
