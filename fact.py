def factorial(num):
    if num < 0:
        print("factorial is not defined for negative numbers")
    result = 1
    for i in range(1,num+1):
        result *= i
    return result


num = 5
print(factorial(num))