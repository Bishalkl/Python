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
 

    

