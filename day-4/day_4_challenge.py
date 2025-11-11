from random import *
name = input("Enter your name: ")
# user_num = int(input("Enter a number between 1 and 100: "))
tries = 8
answer = randint(1, 100)
guesses = 0

while guesses < tries:
    user_num = int(input("Enter a number between 1 and 100: "))
    if user_num < 1 or user_num > 100:
        print("Your number is out of range. Please enter a number between 1 and 100.")
        continue
    guesses += 1
    if user_num < answer:
        print("Too low!")
    elif user_num > answer:
        print("Too high!")
    else:
        print(f"Congratulations {name}! You've guessed the number {answer} correctly in {guesses} tries!")
        break
else:
    print(f"Sorry {name}, you've used all your tries. The correct number was {answer}. Better luck next time!")


