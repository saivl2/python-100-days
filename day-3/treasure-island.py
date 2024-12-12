print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
route = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\" ")

if route == 'left':
    swim_or_wait = input("You're at a lake, swim or wait? ")
    if swim_or_wait == 'wait':
        door = input("At a door which one? (red, blue or yellow) ")
        if door == 'red':
            print('Burned by fire. Game over')
        elif door == 'yellow':
            print('You Win!')
        else:
            print('Game over. Eaten by snake')
    else:
        print('Attacked by trout. Game Over')
else:
    print('Fell into a hole. Game Over')


