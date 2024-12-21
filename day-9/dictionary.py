programming_dictionary = {
    "Bug": "A bug, also known as a defect or error, is an unintended behavior in a software program that deviates from the expected or specified functionality.",
    "Function": "A function is a self-contained block of code that performs a specific task within a program. It typically accepts zero or more input values (arguments) and may return a value as output."
}

print(programming_dictionary['Function'])

programming_dictionary['Loop'] = "A loop is a programming construct that repeats a sequence of instructions until a specific condition is met."

print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary['Bug'] = "A moth in your computer."

print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])