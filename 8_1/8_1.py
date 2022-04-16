import re
class Data:

    @classmethod
    def year(cls):
        data = input(f"Введите дату(00-00-0000):")
        total = re.findall(r'\d+', data)
        new = list(map(int, total))

        return new

    @staticmethod
    def valid(new):

        if new[0] > 31:
            print(f'В месяце не больше 31 дня, введите заново')
        if new[1] > 12:
            print(f'В году не больше 12 месяцев, введите заново')
        if new[2] != 2022:
            print(f'Сейчас 2022 год, введите заново')
        else:
            print(f'Число:{new[0]}\nМесяц:{new[1]}\nГод:{new[2]}')



Data.valid(Data.year())

