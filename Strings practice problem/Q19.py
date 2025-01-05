import re

def replace_special_symbols(s):
    return re.sub(r'[^A-Za-z0-9\s]', '#', s)

# Given string
str1 = "/*Jon is @developer & musician!!"

# Replace special symbols and print the result
modified_string = replace_special_symbols(str1)
print(modified_string)
