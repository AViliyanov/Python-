
with open(r"5_1.txt", "+r", encoding="utf-8") as file:
    for i in file:
        print(f"количество слов в строке:", len(i.split()))

    with open(r"5_1.txt", "+r", encoding="utf-8") as file:
        text = file.read()
        print(f"Строк:", text.count("\n"))
