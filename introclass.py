class details:
    name ="Manish"
    age = 18
    education ="BTech CS AIML and IOT"
    def info(self):
        print(f"{self.name} is {self.age} years old and he is {self.education} student")

obj1 = details()
obj2 = details()
obj2.name = "Alok"
obj2.age = 17
obj2.education = "BTech"
# print(obj1.name)
# print(obj1.age)
# print(obj1.education)
obj1.info()
obj2.info()

