# მომხმარებელს შეაყვანინე რიცხვი. თუ რიცხვი დადებითია, დაბეჭდე Positive, თუ ნულის ტოლია — Zero, სხვა შემთხვევაში — Negative.

number=int(input("please enter your number: "))

if number > 0:
    print("Positive")

elif number == 0:
    print("Zero")

else:
    print("negative")
