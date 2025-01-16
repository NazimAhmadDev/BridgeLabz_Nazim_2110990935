class Stack:
  def __init__(self):
    self.items = []

  def push(self,item):
    self.items.append(item)

  def pop(self):
    self.items.pop()
  
  def is_empty(self):
    return len(self.items) == 0
  
  def display(self):
    return self.items

  def peek(self):
    return self.items[0]

queue = Stack()

queue.push(10)
queue.push(20)
queue.push(30)
queue.push(40)
print("Elements in queue : ",queue.display())

queue.pop()
print("After poping the element : ",queue.display())

print("Top element in the queue : ",queue.peek())