with open(r"text_3.txt", "+r", encoding="utf-8") as file:
    text = file.read()
    res = text.split()
    new_list = {res[i]: float(res[i + 1]) for i in range(0, len(res), 2)}
    total_1 = [i for i, v in new_list.items() if v > 20000]
    my_list = len(new_list.keys())
    summa = sum(new_list.values())
    total = summa / my_list
    print(total)
    print(total_1)



