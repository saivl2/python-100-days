my_bool = 4 < 5 and 10 > 2
print(my_bool)

my_bool = 4 < 5 or 10 < 2
print(my_bool)

my_bool = not(4 <= 5 and 10 > 2)
print(my_bool)

text = "This sentence is short"
print("short" in text and "long" in text)

text = "When something is important enough, you do it even if the odds are against you"

word1 = 'success'
word2 = 'technology'

my_bool = (word1 not in text or word2 not in text)
print(my_bool)