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
