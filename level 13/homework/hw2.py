# while loop-ის გამოყენებით გამოთვალეთ 1-დან 100-მდე ყველა კენტი რიცხვის ჯამი.

total = 0
number = 1

while number <= 100:
    if number % 2 != 0:
        total += number
    number += 1

print(total)