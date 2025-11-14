art = r"""
                   _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
"""
print(art)
print("Welcome to the treasure island\n Your mission is to find the treasure.")
user_input = input("You are at a cross road. Where do you want to go?\n Left or right? ").lower()

if user_input == 'right':
    print('You fell into a hole. Game over')
else:
    direction = input("Swim or wait? ").lower()
    if direction == 'swim':
        print("Attacked by trout. Game over")
    else:
        door = input("Which door? red, blue, yellow ").lower()
        if door == 'red':
            print("Burned by fire. Game Over")
        elif door == 'yellow':
            print('Treasure found. You win!')
        else:
            print('Burned by beasts. Game Over.')
