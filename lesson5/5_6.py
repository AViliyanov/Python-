import re
with open(r"text_6.txt", "r+", encoding="utf-8") as file:
    new = file.read()
    kew = new.split()
    rew = [el for el in kew if el.count(":")]
    bew = [el.replace(":", "") for el in rew]
    with open(r"text_6.txt", "r+", encoding="utf-8") as file:
        new_1 = file.readlines()
        num_1 = []
        num_2 = []
        for i in new_1:
            tottal = re.findall(r'\d+', i)
            num_1.append(tottal)
        for n in num_1:
            tottal_v = list(map(int, n))
            tottal_d = sum(tottal_v)
            num_2.append(tottal_d)
    tottal_key = dict(zip(bew, num_2))
    print(tottal_key)












