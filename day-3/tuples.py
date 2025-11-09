my_tuple = (1,2,3,4)

print(my_tuple)
print(type(my_tuple))

# Tuples are immutable, meaning their values cannot be changed after creation
print(my_tuple[0])  # Accessing the first element
# my_tuple[0] = 10  # This would raise a TypeError

l = list(my_tuple)  # Converting tuple to list
print(type(l))

a , b, c, d = my_tuple  # Unpacking tuple
print(a, b, c, d)