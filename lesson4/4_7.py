def fact(n):
    a = 1
    for el in range(1, n+1):
        a *= el
    yield a
n = int(input("n:"))
for el in fact(n):
    print(el)


