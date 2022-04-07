class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Ручка")

class Pencil(Stationery):
    def draw(self):
        print("Карандаш")

class Handle(Stationery):
    def draw(self):
        print("Маркер")



a = Stationery("Les")
print(a.title)
a.draw()
b = Pen(Stationery)
b.draw()
c = Pencil(Stationery)
c.draw()
d = Handle(Stationery)
d.draw()

