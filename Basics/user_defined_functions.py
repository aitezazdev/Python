def bro():
    print("My bro")

bro()


# Parametric functions
def hello(name, gpa):
    print("hello ", name)
    print("gpa is ", gpa)

hello("zaz", 3.6)


# returning function
def SUM(s):
    return sum(s);

marks = [1,2,3,4,5]
print(SUM(marks))