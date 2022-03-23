a = input("Числа(через запятую):").split(",")
c = str()
b = list(a)
for i in range(1, len(b), 2):
    b[i - 1], b[i] = b[i], b[i - 1]
c = ''.join(b)
print(c)