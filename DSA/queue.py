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
    
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Queue is empty. Cannot peek.")

    def displayQueue(self):
        for item in self.items:
            print(item, end=", ")
        print()


my_queue = Queue()

print("Is the queue empty?", my_queue.isEmpty()) 

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("The elements on queue are : ")
my_queue.displayQueue()

print("Size of the queue:", my_queue.size())

removed_item = my_queue.dequeue()
print("Removed item from the queue:", removed_item)

print("Size of the queue after dequeue:", my_queue.size())

print("Is the queue empty after dequeue?", my_queue.isEmpty())

print("top element is", my_queue.peek())