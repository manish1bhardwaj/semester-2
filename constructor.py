# constructor
# a special method to initialize the class member if needed
# in Python name of the constructor is "__init()"

# class test:
#     def __init__(self):
#         print('This is constructor')
#     def __del__(self):
#         print('this is destructor')

# obj1 = test()
# obj2 = test()
# del obj1

# Destructor
# a default method use to stimulate the object deletion

# class test:
#     def __init__(self):
#         print('This is constructor')
#     def details(self,name):
#         self.name = 'name'
#     def __del__(self):
#         print('This is destructor')



#class variable : shared by all instance
#instance variable : unique to each instance
        
class test:
    #class variable
    x = 10
    def __init__(self,val):
       #instance variable
        self.ab = val

    obj1 = test(30)
    obj2 = test(100)
    print(obj1.x)
    print(obj2.x)
    obj1.ab = 20
    print(obj1.ab)
    print(obj2.ab)