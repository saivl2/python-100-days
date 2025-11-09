my_list = ['a', 'b', 'c', 'd', 'e']
print(type(my_list))

# Mixed data types in a list
another_list = ['hello', 42, 3.14, True]
print(another_list)
print(len(another_list))

# Indexing
print(my_list[0])  # First element
print(my_list[:3])

# Concatenation
print(my_list + another_list)

# Changing elements - mutable
my_list[1] = 'z'
print(my_list)

# Adding elements
my_list.append('f')
print(my_list)

# deleting elements
my_list.remove('c')
print(my_list)

my_list.pop() # removes last element
print(my_list)

my_list.pop(0) # removes element at index 0
print(my_list)

# Sorting
num_list = [5, 2, 9, 1, 5, 6]
num_list.sort() # Sorts in place in ascending order
print(num_list)

num_list.sort(reverse=True) # descending order
print(num_list)

