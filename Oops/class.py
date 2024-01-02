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