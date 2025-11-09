my_text = 'This is a test'
print(my_text[0])
print(my_text[-1])
print(my_text[-3])
print(my_text.index('t')) # Returns the index of the first occurrence of 't'
print(my_text.index('s', 4)) # Returns the index of 't' starting from index 4
print(my_text.index('s', 4, 10)) # Returns the index of 's' between index 4 and 10

# searches from right to left
print(my_text.rindex('t')) # Returns the index of the last occurrence of 't'