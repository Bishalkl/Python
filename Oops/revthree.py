#Single Inheritance: 

#Q1

#class Person
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
#class Employee
class Employee(Person):

    def __init__(self,employee_id,name,age):
        super().__init__(name,age) #calling the constructor from a parent class
        self.employee_id = employee_id
        

    #method
    def display_detail(self):
        print(f"Name: {self.name}, Age : {self.age} and employee_id: {self.employee_id}.")


#creating instance
Person_detail = Employee("Bishal koirala", 12, 120)
Person_detail.display_detail()


#Multiple Inheritance

#Q1

#Class Database
class Database:
    
    def save():
        print("Data saved!!!")


#class Logger
class Logger:
    
    def Log():
        print("Log a message")

#class Application
class Application:
    pass

#class Webapp
class Webapp(Database,Logger):

    def __init__(self,data,message):
        self.data = data
        self.message = message

    def display(self):

        print(f"Data is \'{self.data}\' and message is \"{self.message}\".")
        Database.save()
        Logger.Log()

#create a instance 
first_Webapp = Webapp("dfdfdfjkdisdf+63dfdf45df2","I liked it.")
first_Webapp.display()



#Multileve Inheritance

#class
class Animal:
    def __init__(self,specises):
        self.specises = specises

class Mammal(Animal):
    def __init__(self,name,specises):
        super().__init__(specises)
        self.name = name

class Dog(Mammal):
    def __init__(self,name,specises,breed):
        super().__init__(name,specises)
        self.breed = breed
    
    def detail(self):
        print(f"Specises: {self.specises}.")
        print(f"Name: {self.name}.")
        print(f"Breed: {self.breed}.")


#instance 
Dog1 = Dog("Land","Dog","Husky")
Dog1.detail()


#Hierarchical Inheritance 

import math # importing math calculating
class Shape:

    #init
    def __init__(self,name, color):
        self.name = name
        self.color = color

class Circle(Shape):

    #init
    def __init__(self,radius,name,color):
        super().__init__(name,color)
        self.radius = radius

    #method
    def areaDisplay(self):
        print(f"Name of object is {self.name} and color is {self.color} and The area of circle is {math.pi * self.radius ** 2}.")
        
class Rectangle(Shape):

    #init
    def __init__(self,length,width,name,color):
        super().__init__(name,color)
        self.length = length
        self.width = width
    
    #method
    def areaDisplay(self):
        print( f"Name of object is {self.name} and color is {self.color} and The area of Rectangle is {self.length * self.width}.")
    
# instance 
rectangle = Rectangle(12,34,"First", "Red")
rectangle.areaDisplay()
circle = Circle(12,"Second","Red")
circle.areaDisplay()

#Hybrid
class LivingThing:
    pass

class Animal(LivingThing):
    pass

class Bird(Animal):
    pass

class CanFly:
    
    def fly(self):
        print("Can fly!!!!")
    
class Penguin(Bird,CanFly):
    pass

penguin = Penguin()
penguin.fly()