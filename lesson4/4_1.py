from sys import argv

name, time, money, bonus = argv


def total():
    try:
        zed = ((int(time) * int(money)) + int(bonus))
        return zed
    except ValueError as err:

        print(err)


print(total())
