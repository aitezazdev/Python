class Zaz:
    name = "bro"
    gpa = 3.6
    def info(self):
        print(f"name is {self.name} and gpa is {self.gpa}")

firstOBJECT = Zaz();
firstOBJECT.info()

sec = Zaz();
sec.name = "me"
sec.gpa = 3
sec.info()