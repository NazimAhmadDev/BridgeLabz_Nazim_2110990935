number = int(input("Enter a number: "))

digit_count = 0

if number < 0:
    number = -number


while number > 0:
    digit_count += 1
    number //= 10  

if digit_count == 0:
    digit_count = 1

print(f"The total number of digits is {digit_count}.")
