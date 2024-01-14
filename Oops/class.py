class DemoClass:

    def sum(self): #self
        print(20+30)
    

demoobject=DemoClass()
demoobject.sum()


class Employee:

    def putdata(self): #Method one which is for get a information.
        self.id = int(input("enter Employee id: "))
        self.name = input("enter the Employee name: ")
        self.salary = int((input("enter Employee salary: ")))

    def display(self): #Method two which is for print detail.
        print(f"Id: {self.id}.")
        print(f"Name: {self.name}.")
        print(f"Total salary : Rs.{self.salary}/only.")
    

a = Employee() #creating the object
a.putdata() #calling object for input 
a.display() #calling object for display 


#Polymorphism

import math
from abc import ABC , abstractmethod

#class shape
class Shape(ABC):

    #abstract method
    @abstractmethod
    def area(self):
        pass

#subclass Rectangle
class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
#subclass circle
class Circle(Shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    

#writing the function calculate_total_area
def calculate_total_area(Shapes):
    total_area = 0
    for shape in Shapes:
        total_area +=shape.area()
    return total_area


 # Create instances of Rectangle and Circle
rectangle = Rectangle(length=5, width=3)
circle = Circle(radius=4)

# Add them to a list
shapes_list = [rectangle, circle]

# Calculate the total area
total_area = calculate_total_area(shapes_list)

# Print the result
print("Total area:", total_area)   
