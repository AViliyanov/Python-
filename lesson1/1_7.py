a = int(input("a="))
b = int(input("b="))
d = 2
while (a < b):
    a = a * 1.1
    if a < b:
        d = d+1
    if a > b:
        break
print(d)