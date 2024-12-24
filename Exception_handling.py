try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("This will always run, regardless of exceptions.")
