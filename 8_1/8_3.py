class Type(TypeError):
    def __init__(self, num):
        self.num = num

    my_list = []
    new_number = ""

    while new_number != "q":
        new_number = input("Для выхода нажмите q\nВведите число:")
        try:
            my_list.insert(0, int(new_number))

        except ValueError:
            pass

        print(my_list)


