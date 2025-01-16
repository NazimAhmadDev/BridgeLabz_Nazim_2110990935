from collections import deque

def reverse_first_k(queue,k):
  if k > len(queue) or k <= 0:
    print("Invalid value of k")
    return
  
  stack = []

  for _ in range(k):
    stack.append(queue.popleft())

  
  while stack:
    queue.append(stack.pop())

  
  for _ in range(len(queue) - k):
    queue.append(queue.popleft())

queue = deque([10,20,30,40,50])
k = 3

reverse_first_k(queue,k)

print(list(queue))