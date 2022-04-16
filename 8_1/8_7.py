class MyComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return MyComplex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        new_a = self.a * other.a - self.b * other.b
        new_b = self.b * other.a + self.a * other.b
        return MyComplex(new_a, new_b)


z1 = MyComplex(3,1)
z2 = MyComplex(2,3)


print(f"{complex(z1.a,z1.b)} + {complex(z2.a,z2.b)} = {complex(z1.a,z1.b) + complex(z2.a,z2.b)}")
print(f"{complex(z1.a,z1.b)} * {complex(z2.a,z2.b)} = {complex(z1.a,z1.b) * complex(z2.a,z2.b)}")
