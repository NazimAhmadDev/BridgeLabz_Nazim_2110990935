from queue import Queue

# Create a queue
queue = Queue()

# Add elments
queue.put(10)
queue.put(20)
queue.put(30)

# Remove elements from queue
print(queue.get())
print(queue.get())
print(queue.get())



print("********************************************************************")




from collections import deque


# Create a deque
dq = deque()

# Add the elements to the right
dq.append(1)
dq.append(2)
dq.append(3)


# remove the element from left
print(dq.popleft())
print(dq.popleft())
print(dq.popleft())



print("********************************************************************")



# Creating queue as list
queue = []

queue.append(4)
queue.append(5)
queue.append(6)


# Remove elements
print(queue.pop())
print(queue.pop())
print(queue.pop())


print("********************************************************************")


# Types of Queues

# --> Simple queue
# --> Circular queue
# --> Priority queue

# Simple Queue
from queue import Queue

q = Queue()

q.put(1)
q.put(3)
q.put(5)

print(q.get())



print("********************************************************************")





# Queue using OOPs concept

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    def display(self):
        print(self.queue)
    
    def size(self):
        print(len(self.queue))


q = Queue()

print("Elements present in queue : ")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()

print("After removing the element : ")
q.dequeue()
q.display()



print("***********************************************")




# Circular Queue

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            print(f"Dequeued: {item}")
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            i = self.front
            print("Queue elements: ", end="")
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[self.rear])


cq = CircularQueue(5)


cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()


cq.dequeue()
cq.dequeue()

# Display the queue after dequeuing
cq.display()

# Enqueue more elements
cq.enqueue(60)
cq.enqueue(70)

# Display the final queue
cq.display()
