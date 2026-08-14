# მომხმარებელს შეაყვანინე პროდუქტის რაოდენობა.
# თუ რაოდენობა 0-ზე მეტია, შიგნით შეამოწმე 10-ზე მეტია თუ არა.
# - თუ არის, დაბეჭდე "მარაგი საკმარისია"
# - თუ არა, დაბეჭდე "მარაგი ცოტაა"
# თუ რაოდენობა 0-ია, დაბეჭდე "მარაგი არ არის"

quantity = int(input("Enter the product quantity: "))

if quantity > 0:
    if quantity > 10:
        print("Stock is sufficient")
    else:
        print("Stock is low")
else:
    print("Out of stock")