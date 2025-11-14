print("Welcome to the rollercoaster!")
height = int(input("Enter height: "))
price = 0
if height > 120:
    print('You can ride the rollercoaster')
    age = int(input("Enter age: "))
    if age < 12:
        price = 5
        # print('Please pay $5')
    elif age >= 12 and age <= 18:
        price = 7
        # print('Please pay $7')
    else:
        price = 12
        # print('Please pay $12')
    pic = input("What photo (yes/no)? ")
    if pic == 'yes':
        price += 3
        print(f"You need to pay in total {price}")
    else:
        print(f"You need to pay in total {price}")

else:
    print('Sorry you are not tall enough to ride')
 