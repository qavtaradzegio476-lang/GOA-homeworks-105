
# მომხმარებელს შეაყვანინეთ რიცხვები. თუ შეიყვანს 0-ს, გამოიყენეთ break.
#ყველა დადებითი რიცხვი დაამატეთ total ცვლადში, ხოლო უარყოფითი რიცხვები გამოტოვეთ

total = 0

while True:
    number = int(input("შეიყვანეთ რიცხვი: "))

    if number == 0:
        break

    if number < 0:
        continue

    total += number

print("ჯამი:", total)