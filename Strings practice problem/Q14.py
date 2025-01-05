def split_on_hyphen(s):
    substrings = s.split('-')
    for substring in substrings:
        print(substring)

# Given string
str1 = "Emma-is-a-data-scientist"

# Split and display each substring
split_on_hyphen(str1)
