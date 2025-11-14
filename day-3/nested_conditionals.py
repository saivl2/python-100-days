print("Welcome to the rollercoaster!")
height = int(input("Enter height: "))
if height > 120:
    print('You can ride the rollercoaster')
    age = int(input("Enter age: "))
    if age < 12:
        print('Please pay $5')
    elif age >= 12 and age <= 18:
        print('Please pay $7')
    else:
        print('Please pay $12')
else:
    print('Sorry you are not tall enough to ride')
 