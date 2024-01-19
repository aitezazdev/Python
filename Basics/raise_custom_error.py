user = int(input("Enter number between 1 and 19 : "))

if(user > 19 or user < 1):
    raise ValueError("Enter between 1 and 19")
else:
    print(user)