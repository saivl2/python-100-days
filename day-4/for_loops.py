my_list = ['a', 'b', 'c', 'd']

for letter in my_list:
    letter_number = my_list.index(letter) + 1
    print(letter, letter_number)
print()
for a, b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)