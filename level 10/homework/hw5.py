# მომხმარებელს შეაყვანინე თანხა. თუ თანხა 100 ან მეტია, დაბეჭდე Expensive, თუ 50 ან მეტია — Medium, სხვა შემთხვევაში — Cheap.

price=int(input("please enter your price: "))

if price >= 100:
    print("Expensive")

elif price >= 50:
    print("Medium")

else:
    print("cheap")    