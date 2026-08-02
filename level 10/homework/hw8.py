# მომხმარებელს შეაყვანინე ასაკი. თუ ასაკი 6-ზე ნაკლებია, დაბეჭდე Kindergarten, თუ 18-ზე ნაკლებია — School, სხვა შემთხვევაში — University or Work.

age = int(input("please enter your age: "))

if age < 6:
    print("Kindergarten")
elif age < 18:
    print("School")
else:
    print("University or Work")