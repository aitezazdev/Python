user = input("Enter a number : ")

try:
    print(f"2 * {user} is : {2 * int(user)}");

except Exception as e:
    print("error : ", e)
# except:
#     print("error occured")
finally:
    print("always executed");

print("some code")
print("more code")