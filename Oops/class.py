class DemoClass:

    def sum(self): #self
        print(20+30)
    

demoobject=DemoClass()
demoobject.sum()


class Employee:

    def putdata(self):
        self.id = int(input("enter eimployee id"))
        self.name = input("enter the employee name ")

        self.salary = input(input("enter employee salary"))

    def display(self):
        print(f"Id: {self.id}")
        print(f"Name:  {self.name}")
        print(f"Total salary : {self.salary}")
    


