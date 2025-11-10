for num in list(range(1, 11, 2)):
    print(num)

sum_squares = 0
nums = list(range(1, 16))

for i in nums:
    sum_squares += i ** 2
    
print("Sum of squares from 1 to 15 is:", sum_squares)