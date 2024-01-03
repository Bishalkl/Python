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




        
        
        
