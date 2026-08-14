# 3) შექმენი ცვლადი username და password.
# თუ username სწორია, შიგნით შეამოწმე password.
# - თუ password სწორია, დაბეჭდე "შესვლა წარმატებულია"
# - თუ არა, დაბეჭდე "არასწორი პაროლი"
# თუ username არასწორია, დაბეჭდე "მომხმარებელი ვერ მოიძებნა"

username = input("please enter your username: ")
password = input("plase enter your password: ")

if username == "admin":
    if password == "1234":
        print("შესვლა წარმატებულია")
    else:
        print("არასწორი პაროლი")
else:
    print("მომხმარებელი ვერ მოიძებნა")