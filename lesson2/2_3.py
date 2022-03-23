a = ("зима,весна,лето,осень".split(","))
b = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
c = int(input("Месяц(Число):"))
if c == 12 or c == 1 or c == 2:
   print(b.get(1))
   print(a[0])
elif c == 3 or c == 4 or c == 5:
   print(b.get(2))
   print(a[1])
elif c == 6 or c == 7 or c == 8:
   print(b.get(3))
   print(a[2])
elif c == 9 or c == 10 or c == 11:
   print(b.get(4))
   print(a[3])
else:
   print("Нет такого Месяца")