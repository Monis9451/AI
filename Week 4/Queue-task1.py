from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, x):
        """Adds an element at the rear of the queue."""
        self.queue.append(x)

    def dequeue(self):
        """Removes and returns the front element and returns None if empty."""
        if self.empty():
            return None
        return self.queue.popleft()

    def front(self):
        """Returns the front element without removing it. Returns None if empty."""
        return self.queue[0] if not self.empty() else None

    def rear(self):
        """Returns the rear element without removing it and rturns None if empty."""
        return self.queue[-1] if not self.empty() else None

    def empty(self):
        """Returns True if the queue is empty, otherwise False."""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.queue)

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())
print("Rear:", q.rear())
print("Dequeue:", q.dequeue())
print("Size:", q.size())
print("Is Empty?", q.empty())