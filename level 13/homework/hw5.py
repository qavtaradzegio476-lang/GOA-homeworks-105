# მომხმარებელს შემოატანინეთ რიცხვი n და while loop-ის გამოყენებით გამოთვალეთ 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი.

n = int(input("please enter your number n: "))

total = 0
number = 1

while number <= n:
    if number % 2 == 0:
        total += number
    number += 1

print("ლუწი რიცხვების ჯამი:", total)