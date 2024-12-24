# Handling exception
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Cannot divided by zero!")



# Handling multiple exception
'''
try:
    num = int(input("Enter a number : "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
'''


# Handling with else
'''
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"Result: {result}")      # Else will only print when the try block doesn't through any error
'''




# handling with finally block
'''
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("Cannot divided by zero!")
finally:
    print("Code execution is over")
'''


# Raise / custom exception
'''
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Number cannot be negative.")
except ValueError as e:
    print(f"Error: {e}")
'''



# Catching multiple error in single exception

try:
    # Code that may raise multiple types of exceptions
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError) as e:
    # Handle all specified exceptions
    print(f"Error: {e}")

