def remove_empty_strings(str_list):
    return [s for s in str_list if s]

# Given list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

# Display the original list
print("Original list of strings:", str_list)

# Remove empty strings and display the result
filtered_list = remove_empty_strings(str_list)
print("After removing empty strings:", filtered_list)
