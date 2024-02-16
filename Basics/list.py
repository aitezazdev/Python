list = ["zaz", 14, "bro", 20]

print(list[3])

list[2] = "haha"

print(list)

del list

print(list)

# list comprehension
myList = [x for x in range(10) if x%2 == 0]

print(myList)

b = [a**2 for a in range(10)]
print(b)

# List methods
listZAZ = ["me", "ok", 320]
listZAZ.append(4)
print(listZAZ)

listZAZ.insert(2, 3000)
print(listZAZ)

# sort() --> sort in ascending form
# reverse() --> reverses the list
# index() --> finds the index
# count() --> counts the elemnt in list (repetiotion)
print(listZAZ.count("me"))

# List Functions
# len(list) --> finds length of list
# max(list) --> finds max element in list
# min(list) --> finds min element in list
# sum() --> find sum of elements of list

# seq(list)
mineList = "zaq"

print(list(mineList))


# for loops in Lists
warraList = ["ferrari", "bently", "toyota"]
for car in warraList:
    print(car)