print('Welcome to Python Pizza Deliveries!')
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

need_pepperoni_small = 2
need_pepperoni_large_or_medium = 3

extra_cheese_price = 1

total_bill = 0
if size == 'S':
    total_bill += small_pizza_price
    if pepperoni == 'Y':
        total_bill += need_pepperoni_small
    if extra_cheese == 'Y':
        total_bill += extra_cheese_price


elif size == 'M':
    total_bill += medium_pizza_price
    if pepperoni == 'Y':
        total_bill += need_pepperoni_large_or_medium
    if extra_cheese == 'Y':
        total_bill += extra_cheese_price

else:
    total_bill += large_pizza_price
    if pepperoni == 'Y':
        total_bill += need_pepperoni_large_or_medium
    if extra_cheese == 'Y':
        total_bill += extra_cheese_price
        
print(f"Your total bill is {total_bill}")





