# მომხმარებელს შეაყვანინე ტემპერატურა. თუ ტემპერატურა 30 ან მეტია, დაბეჭდე Hot, თუ 15 ან მეტია — Warm, სხვა შემთხვევაში — Cold.

temperature=int(input("please enter your temperature: "))

if temperature >= 30:
    print("Hot")

elif temperature >= 15:
    print("Warm")

else:
    print("cold")    