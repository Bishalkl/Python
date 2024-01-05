#Question one 

#class 
class Car:

    #method for init
    def __init__(self,model,value):
        self.model = model
        self.value = value


#creating instance 
first_Car = Car(model="Bishal",value="232323")

#display
print(first_Car.model)
print(first_Car.value)

#Q2

#class
class Rectangle:

    #init
    def __init__(self,length,width):
        self.length = length
        self.width = width

    #method for calc and return
    def arearec(self):
        return self.length * self.width
    

#creating a instance
first_rectangle = Rectangle(12,1)

print(f"The are of rectangle is {first_rectangle.arearec()}")

