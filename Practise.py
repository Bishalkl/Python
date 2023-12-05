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

#Assignment Operators:
a = 5 
a +=3
print(a)

#Identity Operators:
list1 = [1,2,3,4,5,6]
list2 = list1

result = list1 is list2
print(result) 

#If-else Statement
c = int(input("Enter the number: "))
if(c >=1):
    print("It is positive number.")
elif(c < 0):
    print("It is negative number.")
else:
    print("It is zero")

#For Loop
d = int(input("Enter the number: "))
for number in range(d-1):
    print(str(d)+"*"+str(number)+" = ",d * number)

#While Loop
import random
correct_number = random.randint(1,10)
guess_number = int(input("Enter the number between 1 to 10: "))

while True:
    if(guess_number == correct_number):
        print("You have guessed correct number !!!")
        break
    elif(guess_number > correct_number):
        print("Too high, Try again.")
        break
    else:
        print("Too low, Try again.")
        break

#Break and Continue:
count = 1
for number in range(2,30,2):
    print(number)
    count +=1

    if count == 10:
        break

#Exception Handling
f = int(input("Enter the first number: "))
g = int(input("Enter the second number: "))

try: 
    result = f / g
    print("The result is ",result)
except:
    print("Sorry we can't divide by number zero, Try again !!!")

