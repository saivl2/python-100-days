from random import *

rand_int = randint(1, 100)
print(f"Random integer between 1 and 100: {rand_int}")

print(uniform(1.5, 10.5))  # Random float between 1.5 and 10.5
print(choice(['apple', 'banana', 'cherry']))  # Random choice from a list
print(shuffle([1, 2, 3, 4, 5]))  # Shuffle a list in place