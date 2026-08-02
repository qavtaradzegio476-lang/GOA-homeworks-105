# მომხმარებელს შეაყვანინე საათი (0-23). თუ საათი 12-ზე ნაკლებია, დაბეჭდე Morning, თუ 18-ზე ნაკლებია — Afternoon, სხვა შემთხვევაში — Evening.
hour=int(input("please enter your hour: "))

if hour < 12:
    print("Morning")

elif hour < 18:
    print("Afternoon")

else:
    print("Evening")    