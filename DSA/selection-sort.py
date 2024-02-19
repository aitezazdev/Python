# def selectionSort(alist):
#     for fillslot in range(len(alist)-1, 0, -1):
#         positionOfMax = 0
#         for location in range(1, fillslot+1):
#             if alist[location] > alist[positionOfMax]:
#                 positionOfMax = location

#         temp = alist[fillslot]
#         alist[fillslot] = alist[positionOfMax]
#         alist[positionOfMax] = temp

# alist = [2,1,3,5,4]
# selectionSort(alist)
# print(alist)

def selectionSort(my_list):
    for outer in range(len(my_list) - 1, 0, -1):
        max_pos = 0

        for inner in range(1, outer):
            if my_list[inner] > my_list[max_pos]:
                max_pos = inner

        temp = my_list[outer]
        my_list[outer] = my_list[max_pos]
        my_list[max_pos] = temp

    return my_list

print(selectionSort([2,1,3,5,4]))