# Practise one
def sum(a, b):
    return a * b

print(sum(1,2))


#Practise two
def facto(input):
    fac = 1
    for i in range(1,input+1):
        fac *= i
    return fac

print(f"The factorial of given number is {facto(10)}")


#Practise three
def checkNum(number):
    if number <= 0:
        return "Enter the correct number."
    if number % 2 == 0:
        return "Even number."
    else:
        return "Odd number."
    
print(checkNum(11))

#Practise four
def reversString(value):
    return value[::-1]    # it is the string manipulation

print(reversString("Bishal koirala"))

#Practise five
sum = 0
def listSum(numbers):
    global sum        # using global keyword
    for i in numbers:
        sum +=i
    return sum

print(listSum([1,2,3,4,5,6,7,8,9,10]))

#Practise six
reversedWord = ""
def palindromeCheck(input):
    global reversedWord
    reversedWord = input[::-1]
    if input == reversedWord:
        return "It is palindrome word"
    else:
        return "It is not palindrome word."

print(palindromeCheck("radar"))

#Practise seven
update_list = []
def filterList(input_list):
    global update_list  #using global keyword 
    update_list =  list(set(input_list))   # list(set()) is use for remove the number of list.
    return update_list

print(filterList([1,2,3,4,5,6,6,6,4,5,3,4,6]))

#Practise eight
def leapCheck(input):
    if (input % 4 == 0 and  input % 100 != 0) or (input % 100 == 0 and input % 400 == 0):
        return "It is a leap year"

    return "It is not leap year"
print(leapCheck(2000))

#Practise nine
n1 = 0
n2 = 1
sum = 0
def fibnacciSequence(input): #0, 1, 1, 2, 3, 5, 8, 13, 21
    global n1, n2, sum
    for i in range(0,input+1):
        print(sum)
        n1 = n2
        n2 = sum
        sum = n1 + n2

fibnacciSequence(5)









    

