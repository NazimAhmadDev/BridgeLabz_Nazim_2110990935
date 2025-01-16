# Using it by taking list
stack = []

stack.append(1)     # push
stack.append(2)
stack.append(3)

print(stack.pop())   # Pop(remove) operation
print(stack)        # Printing the elements inside stack 

# for using peek
top_element = stack[-1]
print("Element at the top : ",top_element)


# Using deque
from collections import deque
stack = deque()
stack.append(4)
stack.append(5)
stack.append(6)

print(stack.pop())
print(stack)



# Printing the elements from stack using for loop

stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

for num in stack:
    print(num)


# printing the elements in single line
stack = [1,2,3,4,5]

print(*stack)


# Implementing stack using class and methods

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if not self.is_empty():
            return f"Element popped from stack is {self.stack.pop()}"
        else:
            return "Stack is empty"

    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return f"Element present at the top of the stack is {self.stack[-1]}"
    
    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())

print(stack.peek())






# Reversing a string using stack

def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str =  ""
    while stack:
        if char in s == " ":
            continue
        else:
            reversed_str += stack.pop()
    
    return reversed_str


s = "hello my name is nazim"
print(reverse_string(s))





# Balanced paranthesis

def balanced_paranthesis(s):
    stack = []

    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


s = "())"
print(balanced_paranthesis(s))



# Sort a stack

def sort_stack(stack):
    stack.sort()

    return stack


stack = [1,2,4,3,5]

sorted_stack = sort_stack(stack)
print(sorted_stack)