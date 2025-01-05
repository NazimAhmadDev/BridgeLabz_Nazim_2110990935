def create_mixed_string(s1, s2):
    result = ''
    for i in range(min(len(s1), len(s2))):
        result += s1[i] + s2[i]
    if len(s1) > len(s2):
        result += s1[len(s2):]
    else:
        result += s2[len(s1):]
    return result

# Given strings
s1 = "Abc"
s2 = "Xyz"

# Create and print the mixed string
print(create_mixed_string(s1, s2))
