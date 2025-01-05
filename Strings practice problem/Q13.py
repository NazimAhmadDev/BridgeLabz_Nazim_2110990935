def find_last_position(s, substring):
    return s.lower().rfind(substring.lower())

# Given string and substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
substring = "Emma"

# Find and print the last position of the substring
last_position = find_last_position(str1, substring)
print(f"Last occurrence of {substring} starts at index {last_position}")
