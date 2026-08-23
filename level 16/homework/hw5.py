# მომხმარებელს შეაყვანინე 10 რიცხვი და თუ რიცხვი არის 0, არ გამოიტანო.

for i in range(10):
    number = int(input("please enter your number: "))

    if number == 0:
        continue
    print(number)