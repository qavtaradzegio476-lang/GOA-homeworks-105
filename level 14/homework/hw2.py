# მომხმარებელს შემოატანინე რიცხვი და დათვალე, რამდენი რიცხვია 1-დან ამ რიცხვამდე ისეთი, რომელიც 3-ზე იყოფა.

number = int(input("please enter your number: "))

count = 0

for i in range(1, number + 1):
    if i % 3 == 0:
        count += 1

print(count)