import re

text = "My phone number is 123-456-7890"

# Find the phone number pattern
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())  # Output: '123-456-7890'




text = "The rain in Spain falls mainly in the plain."

# Replace occurrences of 'rain' with 'snow'
new_text = re.sub(r"rain", "snow", text)
print(new_text)  # Output: 'The snow in Spain falls mainly in the plain.'





text = "Contact us at support@example.com or sales@example.org"

# Extract email addresses
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)  # Output: ['support@example.com', 'sales@example.org']





import string

# Get a list of all letters and digits
print(string.ascii_letters)  # Output: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)  # Output: '0123456789'

# Check if a string is a valid identifier
text = "hello_world"
print(text.isidentifier())  # Output: True
