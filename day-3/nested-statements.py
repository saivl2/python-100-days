print("Welcome to the rollercoaster!")

height = int(input("What is your height: "))
age = int(input("What is your age: "))

if height >= 120:
    print('You can ride it')

    if age <= 12:
        print('Please pay $5')
    elif age <= 18:
        print('Please pay $7')
    else:
        print('Please pay $12')
else:
    print('Too short to ride it')