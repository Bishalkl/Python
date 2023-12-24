
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

#practise three
def palindromeCheck(string):
    string = string.lower()
    reverse_string = string[::-1]
    if(string == reverse_string):
        return f"This {string} is a palindrome string."    
    else:
        return f"This {string} is not a palindrome string."

print(palindromeCheck("bibe"))      


#prac

