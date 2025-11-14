print('Welcome to Python Pizza Deliveries')
size = input("What size pizza do you want? S, M or L ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

pepperoni_small_price = 2
pepperoni_medium_and_large_price = 3

extra_cheese_price = 1

total_price = 0
# Price for small pizza
if size == 's':
    total_price += small_pizza_price
    if pepperoni == 'y':
        total_price += pepperoni_small_price
    if extra_cheese == 'y':
        total_price += extra_cheese
    
# Price for medium pizza
elif size == 'm':
    total_price += medium_pizza_price
    if pepperoni == 'y':
        total_price += pepperoni_medium_and_large_price
    if extra_cheese == 'y':
        total_price += extra_cheese_price
else:
    total_price += large_pizza_price
    if pepperoni == 'y':
        total_price += pepperoni_medium_and_large_price
    if extra_cheese == 'y':
        total_price += extra_cheese_price

print(f"Total Price is ${total_price}")
