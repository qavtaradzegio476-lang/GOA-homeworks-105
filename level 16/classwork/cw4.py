# 4)მომხამარებს შეაყვანინე 5 რიცხვი. თითვეული რიცხვი გამოიტანე მაგრამ თუ რიცხვი უარყოფითი გამოიყენე continue და არ დაბეჭდო.

for i in range(5):
    number = int(input("please enter your number: "))

    if number < 0:
        continue

    print(number)