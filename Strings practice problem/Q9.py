def count_substring_occurrences(str1, substring):
    count = str1.lower().count(substring.lower())
    return count

# Given string and substring
str1 = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"

# Find and print the occurrences of the substring
count = count_substring_occurrences(str1, substring)
print(f"The {substring} count is: {count}")
