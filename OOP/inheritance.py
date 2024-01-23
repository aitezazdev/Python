class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        print(f"name is {self.name} and id is {self.id}")

class Child(Parent):
    def showLanguage(self):
        print("Child class bro")


obj = Parent("parent", 100)
obj.info()

childOBJ = Child("child", 200)
childOBJ.info()
childOBJ.showLanguage()

# obj.showLanguage()      can't do this