# მომხმარებელს შეაყვანინე 5 რიცხვი. თუ რიცხვი 10-ზე მეტია, გამოტოვე და არ გამოიტანო.

for i in range(5):
    number = int(input("please enter your number: "))

    if number > 10:
        continue
    print(number)