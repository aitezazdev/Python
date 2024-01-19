for i in range(1,10):
    print(i)
else:
    print("sorry no i")


# when loop is break else will not execute
for i in range(1,10):
    print(i)
    if i == 3:
        break
else:
    print("sorry no i")
