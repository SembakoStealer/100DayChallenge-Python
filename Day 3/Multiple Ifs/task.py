print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("do ou want to have a photo take? type y for yes and n for no.")
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
