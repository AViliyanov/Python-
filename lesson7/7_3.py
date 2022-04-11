class Cell:
    def __init__(self, numb):
        self.numb = numb

    def __add__(self, other):
        return self.numb + other.numb
    def __sub__(self, other):
        return self.numb - other.numb
    def __mul__(self, other):
        return self.numb * other.numb
    def __truediv__(self, other):
        return self.numb / other.numb
    def make_order (self, row):
        self.row =row
        num = 0
        num_1 = str("*")
        while True:
            num += 1
            if self.numb == num:
                break
            if self.row == num:
                num_1 += "\n"
            if num > self.row:
                self.row += self.row
            num_1 += str("*")
        return num_1

cell = Cell(10)
cell_2 = Cell(7)
print(cell_2.make_order(3))
print(cell + cell_2)
if (cell - cell_2) > 0:
    print(cell - cell_2)
elif (cell - cell_2) < 0:
    print(f"введите число меньше {cell_2.numb} или больше {cell.numb}")
print(cell * cell_2)
print(cell / cell_2)
