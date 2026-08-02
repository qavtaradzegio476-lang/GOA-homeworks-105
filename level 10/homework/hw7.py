# მომხმარებელს შეაყვანინე ორი რიცხვი. თუ პირველი რიცხვი მეორეზე მეტია,
#  დაბეჭდე First number is bigger, თუ ნაკლებია — Second number is bigger, სხვა შემთხვევაში — Numbers are equal.
num1 = int(input("please enter your first number: "))
num2 = int(input("please enter your second number: "))

if num1 > num2:
    print("first number is bigger")

elif num1 < num1:
    print("second number is bigger")

else:
    print("numbers are equal")