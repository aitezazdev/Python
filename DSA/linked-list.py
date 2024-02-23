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

    
    # def add(self, item):
    #     current = self.head
    #     previous = None
    #     while current is not None and current.getData() < item:
    #         previous = current
    #         current = current.getNext()
    #     temp = Node(item)
    #     if previous is None:
    #         temp.setNext(self.head)
    #         self.head = temp
    #     else:
    #         temp.setNext(current)
    #         previous.setNext(temp)

    # def remove(self, item):
    #     current = self.head
    #     previous = None
    #     while current is not None:
    #         if current.getData() == item:
    #             if previous is None:
    #                 self.head = current.getNext()
    #             else:
    #                 previous.setNext(current.getNext())
    #             return
    #         else:
    #             previous = current
    #             current = current.getNext()
    
    # def search(self, item):
    #     current = self.head
    #     found = False
    #     while current is not None and not found:
    #         if current.getData() == item:
    #             found = True
    #         else:
    #             current = current.getNext()
    #     return found

    # def index(self, item):
    #     current = self.head
    #     index = 0
    #     found = False
    #     while current is not None and not found:
    #         if current.getData() == item:
    #             found = True
            
    #         else:
    #             current = current.getNext()
    #             index += 1
    #     if found:
    #         return index
    #     else:
    #         raise ValueError(f"{item} is not in the list")

    # def pop(self):
    #     if self.head is None:
    #         raise IndexError("pop from empty list")
    #     else:
    #         popped_item = self.head.getData()
    #         self.head = self.head.getNext()
    #         return popped_item


class UnorderedList:
    def __init__(self):
        self.head = None

#     def add(self, item):
#         temp = Node(item)
#         temp.setNext(self.head)
#         self.head = temp

#     def remove(self, item):
#         current = self.head
#         previous = None
#         while current is not None:
#             if current.getData() == item:
#                 if previous is None:
#                     self.head = current.getNext()
#                 else:
#                     previous.setNext(current.getNext())
            #     return
            # else:
            #     previous = current
            #     current = current.getNext()


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Connect nodes in an unordered list
unordered_list = UnorderedList()
unordered_list.head = node3
node3.next = node1
node1.next = node2

# # Connect nodes in an unordered list
# unordered_list = UnorderedList()
# unordered_list.add(30)
# unordered_list.add(20)
# unordered_list.add(10)

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

# Connect nodes in an ordered list
# ordered_list = OrderedList()
# ordered_list.add(10)
# ordered_list.add(20)
# ordered_list.add(30)

# Display data in the ordered list
current = ordered_list.head
print("Ordered list is : ")
while current is not None:
    print(current.getData(), end=" -> ")
    current = current.getNext()
print("None")
