import random

user_choice = int(input("What do you choose Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer_choice = random.randint(0,2)

rock = 0
paper = 1
scissors = 2

if user_choice == computer_choice:
    print('Tie!')
elif (user_choice == rock and computer_choice == paper) or \
     (user_choice == paper and computer_choice == scissors) or \
     (user_choice == scissors and computer_choice == rock):
    print('Computer Wins!')
elif (user_choice == paper and computer_choice == rock) or \
     (user_choice == scissors and computer_choice == paper) or \
     (user_choice == rock and computer_choice == scissors):
    print("User Wins!")