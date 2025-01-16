stack = [1,2,3,4,5]

temp = []

n = len(stack)

mid = int(n/2)

for i in range(mid):
    temp.append(stack.pop())

stack.pop()

while temp:
    stack.append(temp.pop())

print(stack)