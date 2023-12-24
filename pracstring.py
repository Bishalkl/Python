
#practise one
def reverseString(string): #creating the fuction
    return string[::-1]  #returning the value after reversing the string 

print(reverseString("Bishal koirala"))

#practise two
def countVowels(string): 
    VowelsList = ['a','e','i','o','u'] 
    count = 0 
    string = string.lower() 
    for i in string:
        for x in VowelsList:
            if i == x:
                count += 1

    return count  

print(countVowels("Bishal"))  
                



