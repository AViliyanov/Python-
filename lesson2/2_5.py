a = int(input("Рейтинг:"))
my_list = [20, 15, 10, 6, 2]

while a:
    for el in range(len(my_list)):
        if my_list[0] < a:
            my_list.insert(0, a)
            break
        elif my_list[-1] > a:
            my_list.append(a)
            break
        elif my_list[el] == a:
            my_list.insert(el+1, a)
            break
        elif my_list[el] > a and my_list[el + 1] < a:
            my_list.insert(el+1, a)
            break
    print(my_list)
    break