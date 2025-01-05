from collections import Counter

def count_characters(s):
    return dict(Counter(s))

# Given string
str1 = "Apple"

# Count the occurrences of each character
char_count = count_characters(str1)

# Print the result
print(char_count)
