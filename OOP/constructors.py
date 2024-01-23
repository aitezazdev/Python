class Person:
    def __init__ (self, name , semester):
        self.name = name
        self.semester = semester

    def info(self):
        print(f"name is {self.name} and semester is {self.semester}")

a = Person("zaz", 3)
a.info()