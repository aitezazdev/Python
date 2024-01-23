# Public
class Checking:
    def __init__(self):
        self.name = "Zaz"

a = Checking()
print(a.name)


# Private
class Checking:
    def __init__(self):
        self.__name = "Zaz"

a = Checking()
# print(a.name) # can't be accessed


# Private access method
class Checking:
    def __init__(self):
        self.__name = "Zaz"

a = Checking()
print(a._Checking__name) # can be accessed