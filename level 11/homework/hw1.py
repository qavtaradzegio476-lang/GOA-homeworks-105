# შექმენი ცვლადი balance = 1000.
# მომხმარებელს შეაყვანინე თანხა.
# თუ თანხა დადებითია, შიგნით შეამოწმე ბალანსზე მეტია თუ არა.
# - თუ არა, დაბეჭდე "თანხა წარმატებით გაიტანეთ"
# - თუ მეტია, დაბეჭდე "არასაკმარისი ბალანსი"
# თუ თანხა 0 ან უარყოფითია, დაბეჭდე "არასწორი თანხა"

balance = 1000
price = int(input("Please enter your price: "))

if price > 0:
    if price <= balance:
        print("Withdrawal successful")
    else:
        print("Not enough balance")
else:
    print("Incorrect price")