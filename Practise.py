#Arithimetic Operators. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The sum is ", num1+num2)
print("The difference is ", num1-num2)
print("The product is ", num1*num2)
print("The quotient is ", num1 // num2)

#Comparison Operators.
age = int(input("Enter your age: "))
if(age >= 18):
    print("You are eligible to vote !!!")
else:
    print("You are not eligible to vote !!!")

# Logical Operators.
number = int(input("Enter the number: "))
if(number % 2 == 0 and number % 3 == 0):
    print("It is divisible number.")
else:
    print("It is not divisible.")