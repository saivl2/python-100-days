num1 = 20
num2 = 30.5
# Implicitt conversion - Python automatically converts num1 to float
num1 = num1 + num2
print(type(num1))
print(type(num2))
print()
# Explicit conversion - converting num2 to int
num2 = int(num2)
print(type(num2))
print(num2)

age = int(input("Enter your age: "))
print(age * 2)