class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Create a new queue
my_queue = Queue()

# Check if the queue is empty
print("Is the queue empty?", my_queue.isEmpty())  # Output: True

# Enqueue some items
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Check the size of the queue
print("Size of the queue:", my_queue.size())  # Output: 3

# Dequeue an item
removed_item = my_queue.dequeue()
print("Removed item from the queue:", removed_item)  # Output: 10

# Check the size of the queue after dequeue
print("Size of the queue after dequeue:", my_queue.size())  # Output: 2

# Check if the queue is empty after dequeue
print("Is the queue empty after dequeue?", my_queue.isEmpty())  # Output: False