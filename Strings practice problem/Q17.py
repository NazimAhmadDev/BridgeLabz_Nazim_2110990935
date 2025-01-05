def remove_non_integers(s):
    return ''.join([char for char in s if char.isdigit()])

# Given string
str1 = "I am 25 years and 10 months old"

# Remove all non-integer characters and print the result
numbers_only = remove_non_integers(str1)
print(numbers_only)
