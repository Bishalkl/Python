#Question

# class
class BankAccount: 

    #self init
    def __init__(self,account_number,initial_balance):
        self.__account_number  = account_number
        self.__initial_balance = initial_balance

    #deposit
    def deposit(self,amount):
        self.amount = amount
        self.__initial_balance += self.amount
        return  f" You have deposit{self.amount}, Now you have Rs.{self.__initial_balance}.00/only."

    #withdraw
    def withdraw(self,amount):
        self.amount = amount
        if(self.__initial_balance >= self.amount ):
            self.__initial_balance -= self.amount
            return f" You have withdraw{self.amount}, Now you have Rs.{self.__initial_balance}.00/only."
        else:
            print(f"You have no enough balance!!")


    #getter
    def get_balance(self):
        return self.__initial_balance
    
    

#creating instance 
my_acount = BankAccount("12635347",50000)

print(my_acount.deposit(10000))

print(my_acount.withdraw(5000))


#question2

#class 
class Book:

    #init
    def __init__(self,title,author,price):
        self.__title = title
        self.__author = author
        self.__price = price

    #method for price 
    def set_price(self,new_price):
        self.new_price = new_price
        return new_price
        
    
    #get
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_price(self):
        return self.__price


#instance 
# Creating an instance
Book1 = Book("Statistics and Probability", "Dr.James rd jackson", 2000)

print(f"Title: {Book1.get_title()}. \nAuthor: {Book1.get_author()}. \nOld Price: Rs.{Book1.get_price()}/only. \nNew Price: Rs.{Book1.set_price(1500)}/only.")



