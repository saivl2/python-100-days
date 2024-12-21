import logo
import os
print(logo.logo)

bidders = {}


while True:
    name = input("What is your name? ")
    amount = int(input("What is your bid? $"))
    bidders[name] = amount
    
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if more_bidders == 'no':
        break
    

bidding_amount = bidders.values()
highest_bid = max(bidding_amount)


for name, amount in bidders.items():
    if amount == highest_bid:
        print(f"The winner is {name} with a bid of ${amount}.")
        break
