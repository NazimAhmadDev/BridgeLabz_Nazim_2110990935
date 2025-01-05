import re

def find_words_with_alphabets_and_numbers(s):
    words = s.split()
    result = [word for word in words if re.search(r'[a-zA-Z]', word) and re.search(r'\d', word)]
    return result

# Given string
str1 = "Emma25 is Data scientist50 and AI Expert"

# Find words with both alphabets and numbers
words_with_both = find_words_with_alphabets_and_numbers(str1)
print(' '.join(words_with_both))
