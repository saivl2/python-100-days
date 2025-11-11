my_list = ['a', 'b', 'c', 'd']

index = 0

for item in my_list:
    print(index, item)
    index += 1
print()
# Using enumerate to achieve the same result
for index, item in enumerate(my_list):
    print(index, item)

print(list(enumerate(my_list)))