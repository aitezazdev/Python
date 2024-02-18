def bubbleSort(myList):
    for num in range(len(myList)-1, 0, -1):
        for i in range(num):
            if myList[i] > myList[i + 1]:
                temp = myList[i]
                myList[i] = myList[i + 1]
                myList[i + 1] = temp

    return my_list

my_list = [2,1,3,5,4]
print( bubbleSort(my_list))