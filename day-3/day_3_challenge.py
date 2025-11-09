text = input("Enter text: ").lower()
l1, l2, l3 = input("Enter three letters separated by spaces: ").split()

# Count occurrences of each letter
count1 = text.count(l1)
count2 = text.count(l2)
count3 = text.count(l3)

print(f"'{l1}' occurs {count1} times.")
print(f"'{l2}' occurs {count2} times.")
print(f"'{l3}' occurs {count3} times.")
print()
# How many words are in the text?
words = text.split()
print(f"The text contains {len(words)} words.")
print()
# First and last letter
first = text.split()[0][0]
last = text.split()[-1][-1]
print(f"The first letter of the text is '{first}'.")
print(f"The last letter of the text is '{last}'.")

# Text in reverse order
reverse_text = words.reverse()
reverse_text = ' '.join(words)
print(f"Reversed text: {reverse_text}")
# Check if 'python' is in the text
print('python' in text)

