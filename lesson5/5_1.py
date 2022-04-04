with open(r"5_1.txt", "w+", encoding="utf-8") as file:
    text = input("text:") + "\n"
    while text:
        file.write(text)
        text = input("text:") + "\n"
        if text == "\n":
            break










