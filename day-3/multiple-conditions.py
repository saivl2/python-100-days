print("Welcome to the rollercoaster!")

height = int(input("What is your height: "))
age = int(input("What is your age: "))
bill = 0

if height >= 120:
    print('You can ride it')

    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    need_photo = input("Do you want a photo taken? ")
    if need_photo == 'yes':
        bill += 3
        print(f"You need to pay : {bill}")
    else:
        print(f"You need to pay: {bill}")

else:
    print('Too short to ride it')