Number = int(input("Number="))
x = 1

while (Number):
    if (Number % 10 > x):
        x = Number % 10
    Number //= 10
print(x)
