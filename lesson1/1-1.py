Gender = str(input("Gender="))
Foot_size = int(input("Foot size:"))
if Gender == "Man":
    print("Hello people!")
elif Gender == "Woman":
    print("Hello people!")
else:
    print("Sorry, you sure?")
if Foot_size <= 42:
    print("Ms")
elif Foot_size > 42:
    print("Mr")
