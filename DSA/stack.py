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
    
    def displayStack(self):
        for item in self.items:
            print(item, end=", ")
        print()
    
stack = Stack()

print("Is the stack empty?", stack.isEmpty())

stack.push(1)
stack.push(2)
stack.push(3)

print("The elements on stack are : ")
stack.displayStack()

print("Size of the stack:", stack.size())

print("Top element of the stack:", stack.peek())

print("Popped element:", stack.pop())

print("Size of the stack after popping:", stack.size())