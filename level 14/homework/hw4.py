# მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათ შორის ყველაზე დიდი რიცხვი.

max_number = int(input("please enter your number: "))

for i in range(4):
    number = int(input("please enter your number: "))

    if number > max_number:
        max_number = number

print("ყველაზე დიდი რიცხვია:", max_number)