my_set = set([1,2,3,4,5])
print(type(my_set))
print(my_set)

other_set = {1,2,3, 3, 4, (1,2,3)}

print(other_set)
print(2 in my_set)

# Set joining
s1 = {1,2,3}
s2 = {3,4,5}

print(s1.union(s2))
s1.add(5)
print(s1)
s1.remove(3)
print(s1)
s1.discard(10)  # Does not raise an error if the element is not found
print(s1)
s1.add(2)  # Adding an existing element does nothing
print(s1)

s1.pop()  # Removes and returns an arbitrary element
print(s1)
s1.clear()  # Empties the set
print(s1)

