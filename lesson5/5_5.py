with open(r"text_5.txt", "w+", encoding="utf-8") as file:

    numbers = input("numb:")
    new = file.write(numbers)
    new_3 = file.seek(0)
    new_1 = file.read()
    new_4 = new_1.split()
    numb = 0
    new_list_1 = [numb + int(new_4[i]) for i in range(len(new_4))]
    print(sum(new_list_1))
