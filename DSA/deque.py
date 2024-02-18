class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def displayDeque(self):
        for item in self.items:
            print(item, end=' ')
        print()


my_deque = Deque()

my_deque.addFront(1)
my_deque.addRear(2)
my_deque.addFront(3)
my_deque.addRear(4)

print("Elements of the deque:")
my_deque.displayDeque()

print("Size of the deque:", my_deque.size())

removed_front = my_deque.removeFront()
removed_rear = my_deque.removeRear()

print("Removed from the front:", removed_front)
print("Removed from the rear:", removed_rear)

print("Size of the deque after removal:", my_deque.size())

print("Is the deque empty?", my_deque.isEmpty())