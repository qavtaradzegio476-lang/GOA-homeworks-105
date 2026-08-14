# მომხმარებელს შეაყვანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ რიცხვები total ცვლადში
# . 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი.

total = 0

while True:
    number = int(input("please enter your number: "))

    if number == 0:
        break

    total += number

print("ჯამი:", total)
