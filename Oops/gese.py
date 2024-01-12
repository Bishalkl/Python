class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    # Getter for full name
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age with validation
    @age.setter
    def age(self, value):
        if 0 <= value <= 120:  # Assuming a reasonable age range
            self._age = value
        else:
            print("Invalid age. Age must be between 0 and 120.")

    # Deleter for age
    @age.deleter
    def age(self):
        print(f"Deleting age for {self.full_name}")
        del self._age

# Example usage:
person = Person("John", "Doe", 30)

# Using the getter for full name
print("Full Name:", person.full_name)

# Using the getter for age
print("Age:", person.age)

# Using the setter for age
person.age = 35

# Attempting to set an invalid age
person.age = 150  # This will print an error message

# Using the deleter for age
del person.age  # This will print a message about deleting the age


#Exercies

class BankAccount:
    
    def __init__(self, account_holder, balance, is_locked):
        self.__account_holder = account_holder
        self.__balance = balance
        self.__is_locked = is_locked

    @property
    def account_holder(self):
        return self.__account_holder
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def is_locked(self):
        return self.__is_locked

    @account_holder.setter
    def account_holder(self, value):
         self.__account_holder = value
    
    @balance.setter
    def balance(self, value):
        self.__balance = value
    
    @is_locked.setter
    def is_locked(self, value):
         self.__is_locked = value
    
    def unlock_account(self):
        self.__is_locked = False

    def withdraw(self, amount):
        if not self.__is_locked and 0 < amount <= self.__balance:
            self.__balance -= amount 
            print(f"Total balance became {self.__balance} and amount you have withdrawn is {amount}")
        else:
            print("Not enough balance or account is locked!!!")

    def lock_account(self):
        self.__is_locked = True 

    def deposit(self, amount):
        if not self.__is_locked and amount > 0:
            self.__balance += amount
            print(f"You have deposited {amount} and became {self.__balance}")
        else:
            print("You don't have enough balance or the account is locked.")

    def __str__(self):
        return f"The account holder is {self.__account_holder}, current value is {self.__balance}, and locked is {self.__is_locked}"
    
# Example usage:
account1 = BankAccount("Bishal Koirala", 100000, False)
account1.withdraw(500)
account1.deposit(200)
account1.lock_account()

# Attempt to withdraw and deposit from a locked account
account1.withdraw(100)
account1.deposit(50)

account1.unlock_account()
account1.withdraw(100)
account1.deposit(50)

print(account1)

        

    
        
