from shutil import copyfile
from googletrans import Translator
with open(r"text_4.txt", "r+", encoding="utf-8") as file:
    my_list = file.read()
    new_list = Translator()
    list_1 = new_list.translate(my_list, dest="ru")
    with open(r"text_4_1.txt", "w", encoding="utf-8") as file:
        file.write(list_1.text)

    print(list_1.text)
