class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"{self.name} {self.surname} {self.position}")

    def get_total_income(self):
        print(sum(self._income.values()))


a = Position("Alex", "Vilyanov", "Junior", 100000, 20000)
a.get_full_name()
a.get_total_income()
