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


