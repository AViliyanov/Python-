class Car:
    def __init__(self, speed, color, name, is_police, now_speed):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.now_speed = now_speed

    def go(self):
        print("поехала")

    def stop(self):
        print("остановилась")

    def turn(self):
        print(f"повернула")

    def show_speed(self):
        print(f"Ваша текущая  скорость: {self.now_speed}\n")

    def all(self):
        print(f"Name: {self.name}\nColor: {self.color}\nSpeed: {self.speed}")


class Sportcar(Car):
    def __init__(self, speed, color, name, is_police, now_speed):
        super().__init__(speed, color, name, is_police, now_speed)

    def all(self):
        print(f"Name: {self.name}\nColor: {self.color}\nSpeed: {self.speed}")


class Policecar(Car):
    def __init__(self, speed, color, name, is_police, now_speed):
        super().__init__(speed, color, name, is_police, now_speed)

    def all(self):
        print(f"Name: {self.name}\nColor: {self.color}\nSpeed: {self.speed}")



class Towncar(Car):
    def __init__(self, speed, color, name, is_police, now_speed):
        super().__init__(speed, color, name, is_police, now_speed)

    def show_speed(self):
        if self.now_speed > 60:
            print(f"Вы превысили скорость")
        elif self.now_speed <= 60:
            print(f"Ваша текущая  скорость: {self.now_speed}\n")

    def all(self):
        print(f"Name: {self.name}\nColor: {self.color}\nSpeed: {self.speed}")

class Workcar(Car):
    def __init__(self, speed, color, name, is_police, now_speed):
        super().__init__(speed, color, name, is_police, now_speed)

    def show_speed(self):
        if self.now_speed > 40:
            print(f"Вы превысили скорость")
        elif self.now_speed <= 40:
            print(f"Ваша текущая  скорость: {self.now_speed}")

    def all(self):
        print(f"Name: {self.name}\nColor: {self.color}\nSpeed: {self.speed}")

a = Car(250, "Gold", "Mersedes", False, 80)
a.all()
a.show_speed()
b = Towncar(220, "Black", "BMW", False, 65)
b.all()
print(b.now_speed)
b.show_speed()
c = Workcar(220, "Blue", "LADA", False, 45)
c.all()
print(c.now_speed)
c.show_speed()

d = Sportcar(300, "Red", "Bugatti", False, 45)
d.all()

e = Policecar(2200, "Green", "Ford", True, 45)
e.all()









