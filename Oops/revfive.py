#question one 
from abc import ABC ,abstractmethod

class Vehicle(ABC):

    #abstract method
    @abstractmethod
    def display_info(self):
        pass

#subclass car
class Car(Vehicle):

    def __init__(self,name,model):
        self.name = name
        self.model = model

    #overriding
    def display_info(self):
        return f"Name: {self.name}.\n Model: {self.model}.\n It is fast."
    
#subclass Bicycle
class Bicycle(Vehicle):

    def __init__(self,name,model):
        self.name = name
        self.model = model
        
    #Overriding
    def display_info(self):
        return f"Name: {self.name}.\n Model: {self.model}.\n It is slow."
    

#function
def show_vehicle_info(total_Vechile):
    for vechile in total_Vechile:
        print(f" {vechile.display_info()}")
        print("\n")

#instance 
c1 = Car("lambo","123jfh")
b1 = Bicycle("hero","hdfhff")

total_Vechile = [c1,b1]

print(f"The vlaue is total vechile: .")
show_vehicle_info(total_Vechile)


#Question 2

#class 
class ComplexNumber:

    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    #overload
    def __add__(self,other):
        add_real = self.real + other.real
        add_img = self.img + other.img
        return ComplexNumber(add_real, add_img)

    #overload   
    def __mul__(self,other):
        multi_real = self.real * other.real - self.img * other.img
        multi_img = self.img * other.img + self.real * other.real
        return ComplexNumber(multi_real, multi_img)
    
    def __str__(self):
        return f"{self.real} + {self.img}"
#instance 
a1 = ComplexNumber(12,1)
a2 = ComplexNumber(12,1)

result_add = a1 + a2
result_multi = a1 * a2   

print(f"The result_add = {result_add}.")
print(f"The result_multi = {result_multi}")

