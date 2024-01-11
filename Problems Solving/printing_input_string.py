user = input("Enter any string : ")

count = 0

for i in user:
    print(i)

    # if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
    if i.lower() in "aeiou":  # also can be written in this form
        count += 1

print("count is : ", count)