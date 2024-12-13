import random
import my_module

# Random integers
v1 = random.randint(1,10)

print(v1)
print(my_module.my_num)

# Random floating-point

v2 = random.random() # random number between 0 to 1
print(v2)

v3 = random.uniform(1,10) # random float number from the given range
print(v3)

