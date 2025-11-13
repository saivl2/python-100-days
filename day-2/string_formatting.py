# rounding
bmi = 84 / 1.65 ** 2
print(bmi)

print(int(bmi))

# round(number, ndigits), it rounds the number to the nearest whole number. 
# If the decimal part is 0.5 or higher, it rounds up, while if it's lower than 0.5, it rounds down.
print(round(bmi))
print(round(bmi, 2))

# f-strings
print(f"BMI is {round(bmi)}")