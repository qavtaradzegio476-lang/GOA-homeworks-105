# 1. მომხმარებელს შემოატანინე რიცხვი.
# თუ რიცხვი დადებითია, დაბეჭდე `"დადებითი რიცხვია"`.
# თუ რიცხვი უარყოფითია, დაბეჭდე `"უარყოფითი რიცხვია"`.
# სხვა შემთხვევაში, დაბეჭდე `"ნულის ტოლია"`.
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is equal to zero.")