import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        """Insert an element with a given priority."""
        heapq.heappush(self.heap, (priority, value))

    def dequeue(self):
        """Remove and return the element with the highest priority."""
        if self.empty():
            return None
        return heapq.heappop(self.heap)[1]

    def front(self):
        """Return the element with the highest priority without removing it."""
        return self.heap[0][1] if not self.empty() else None

    def empty(self):
        """Check if the priority queue is empty."""
        return len(self.heap) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.heap)

pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 2)

print("Front:", pq.front())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Size:", pq.size())
