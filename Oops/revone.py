
####Q1

#creating a class 
class Rectangle:

    def __init__ (self, length,width):
        self.length = length
        self.width = width

    #creating a method name area for calculation area
    def area(self):
        return self.length * self.width
    

#creating instance 
my_rectangle = Rectangle(12.3,34.4)

#calling method
print(f"The area of rectangle is {my_rectangle.area()}.")


###Q2

#creating the class 
class Person:

    #initializes the attributes:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #creating the method for passing a parameter
    def detail(self):
        return f"Name is {self.name} and Age is {self.age}."

#creating instance 
personOne = Person("Alice",20)
persontwo = Person("Bob", 30)
print(personOne.detail())
print(persontwo.detail())
        
        
        
