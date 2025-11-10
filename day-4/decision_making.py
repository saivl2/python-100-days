pet = 'dog'

if pet == 'cat':
    print('You have a cat!')
elif pet == 'dog':
    print('You have a dog!')
else:
    print('You have a different kind of pet.')

age = 20
school_grade = 9

if age < 18:
    print('You are a minor.')
    if school_grade < 6:
        print('You are in elementary school.')
    elif school_grade < 9:
        print('You are in middle school.')
    else:
        print('You are in high school.')
elif age < 65:
    print('You are an adult.')
else:
    print('You are a senior citizen.')