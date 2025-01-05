def middle_three_chars(s):
    middle_index = len(s) // 2
    return s[middle_index - 1:middle_index + 2]

# Case 1
str1 = "JhonDipPeta"
print(middle_three_chars(str1))

# Case 2
str2 = "JaSonAy"
print(middle_three_chars(str2))
