import json
with open(r"text_7.txt", "r+", encoding="utf-8") as file:
    total = []
    new_1 = file.readlines()
    new_2 = [el.split() for el in new_1]
    dict = {new_2[d][0]: int(new_2[d][2]) - int(new_2[d][3]) for d in range(0, len(new_2),)}
    total.append(dict)
    new = dict.values()
    dict_1 = [v for el, v in enumerate(new) if v > 0]
    dict_2 = {"average_profit": sum(dict_1) // len(dict_1)}
    total.append(dict_2)
    with open(r"text_77.json", "+w", encoding="utf-8") as file:
        json.dump(total, file, ensure_ascii=False)
    print(total)
