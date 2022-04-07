class Road:

    def __init__(self, lenght, width):
        self.__length = lenght
        self.__width = width

    def massa(self):
            formula = self.__width * self.__length * 25 * 1
            print(f'{self.__width}м * {self.__length}м * 25кг * 1см = {formula}тонн')


total = Road(int(input('length(metr):')), int(input('width(metr):')))
total.massa()


