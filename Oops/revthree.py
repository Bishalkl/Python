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
