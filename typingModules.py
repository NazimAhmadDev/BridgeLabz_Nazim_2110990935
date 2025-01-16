from typing import Union

def add(a: int, b:int) -> int:
    return a+b

# print(add(1,'2'))     This wil throw an error 
print(add(1,2))


def greet(name : str) -> str:
    return f"Hello {name}!"

print(greet("Nazim")) 



# List and Dictonary

from typing import List, Dict

def square_numbers(nums: List[int]) -> Dict[int, int]:
    return {n: n ** 2 for n in nums}

# Example usage
numbers = [1, 2, 3, 4, 5]
squared_dict = square_numbers(numbers)

# Print the result
print(squared_dict)

