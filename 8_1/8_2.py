class Zerodivision(ZeroDivisionError):
    def __init__(self, num):
        self.num = num

    num_1 = input(f"Делимое:")
    num_2 = input(f"Делитель:")

    try:
        num_3 = int(num_1) / int(num_2)

    except ZeroDivisionError:
        print("На 0 делить нельзя")
    except ValueError:
        print("Введите число")
    else:
        print(f"Ответ: {num_3}")






