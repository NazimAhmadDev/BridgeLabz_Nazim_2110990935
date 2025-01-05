def arrange_characters(s):
    lower_case = ''.join([char for char in s if char.islower()])
    upper_case = ''.join([char for char in s if char.isupper()])
    return lower_case + upper_case

# Given string
str1 = "PyNaTive"

# Arrange and print the result
print(arrange_characters(str1))
