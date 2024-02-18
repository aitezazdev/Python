def BinarySearch(myList, item):
    first = 0
    last = len(myList) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if myList[midpoint] == item:
            found = True
        else:
            if item < myList[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    return found

list = [2, 12, 20, 34, 45]
print(BinarySearch(list, 11))
print(BinarySearch(list, 45))