
from itertools import count, cycle, takewhile

new = [*takewhile(lambda l: l != 11, count(3))]
c = 0
for el in cycle(new):
    if c > 5:
        break
    c += 1
    print(el)


print(new)


