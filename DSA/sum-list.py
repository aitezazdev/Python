def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))

# Fifth Iteration returns 9.
# Fourth Iteration returns 7 + 9 = 16.
# Third Iteration returns 5 + 16 = 21.
# Second Iteration returns 3 + 21 = 24.
# First Iteration returns 1 + 24 = 25.

# First Iteration:
# Initial call: listsum([1, 3, 5, 7, 9])
# Since the length of the list is greater than 1, the else block is executed.
# The function returns 1 + listsum([3, 5, 7, 9]).

# Second Iteration:
# Recursive call: listsum([3, 5, 7, 9])
# Since the length of the list is greater than 1, the else block is executed.
# The function returns 3 + listsum([5, 7, 9]).