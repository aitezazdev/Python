class Stack:    
    def __init__(self):
        self.items = []  # inilitizes item as empty list
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
stack = Stack()

# Check if the stack is empty
print("Is the stack empty?", stack.isEmpty())  # Output: True

# Push some values onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Check the size of the stack
print("Size of the stack:", stack.size())  # Output: 3

# Peek at the top element of the stack
print("Top element of the stack:", stack.peek())  # Output: 3

# Pop an element from the stack
print("Popped element:", stack.pop())  # Output: 3

# Check the size of the stack after popping
print("Size of the stack after popping:", stack.size())  # Output: 2