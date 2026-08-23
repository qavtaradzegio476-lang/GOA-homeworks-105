# მომხმარებელს შემოატანინე 5 რიცხვი და for loop-ის გამოყენებით იპოვე მათი ჯამი.

total = 0

for i in range(5):
    number = int(input("please enter your number: "))
    total = total + number

print("ჯამი არის:", total)