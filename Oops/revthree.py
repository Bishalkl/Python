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
class 
