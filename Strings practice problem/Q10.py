def sum_and_average_of_digits(s):
    digits = [int(char) for char in s if char.isdigit()]
    total_sum = sum(digits)
    average = total_sum / len(digits) if digits else 0
    return total_sum, average

# Given string
str1 = "PYnative29@#8496"

# Calculate sum and average
total_sum, average = sum_and_average_of_digits(str1)

# Print the results
print(f"Sum is: {total_sum}")
print(f"Average is: {average}")
