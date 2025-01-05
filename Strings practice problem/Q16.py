import re

def remove_special_symbols(s):
    return re.sub(r'[^A-Za-z0-9\s]', '', s)

# Given string
str1 = "/*Jon is @developer & musician"

# Remove special symbols and print the result
cleaned_string = remove_special_symbols(str1)
print(cleaned_string)
