name = "John"
age = 25
height = 6.2
print("Name: %s, Age: %d, Height: %0.2f" % (name, age, height))

# Using .format() Method:
name = "John"
age = 25
height = 6.2
print("Name: {}, Age: {}, Height: {:.2f}".format(name, age, height))

# Using f-Strings (Python 3.6 and newer):
name = "John"
age = 25
height = 6.2
print(f"Name: {name}, Age: {age}, Height: {height:.2f}")