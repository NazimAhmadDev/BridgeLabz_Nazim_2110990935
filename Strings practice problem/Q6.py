def count_characters(s):
    chars = digits = symbols = 0
    for char in s:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1
    return chars, digits, symbols

# Given string
str1 = "P@#yn26at^&i5ve"

# Count and display the result
chars, digits, symbols = count_characters(str1)
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbol = {symbols}")
