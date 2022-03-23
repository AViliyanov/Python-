seconds = int(input("How many seconds:"))
hour = seconds // 3600
minute = seconds % 3600
minute_1 = int(minute) // 60
second = seconds % 60
print(f'{hour:02d}:{minute_1:02d}:{second:02d}')
