class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

class UnorderedList:
    def __init__(self):
        self.head = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes in an unordered list
unordered_list = UnorderedList()
unordered_list.head = node3
node3.next = node1
node1.next = node2

# Display data in the unordered list
current = unordered_list.head
print("unordered list is : ")
while current is not None:
    print(current.getData(), end=" -> ")
    current = current.getNext()
print("None")

# Connect nodes in an ordered list
ordered_list = OrderedList()
ordered_list.head = node1
node1.next = node2
node2.next = node3
node3.next = None

# Display data in the ordered list
current = ordered_list.head
print("Ordered list is : ")
while current is not None:
    print(current.getData(), end=" -> ")
    current = current.getNext()
print("None")