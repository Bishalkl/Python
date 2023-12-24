
#practise one
def reverseString(string): 
    return string[::-1]  

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


#practise four
string1 = str(input("Enter the first string: "))
string2 = str(input("Enter the second string: "))
first_method = string1 +" "+ string2
second_method = f"{string1} {string2}"
print(first_method)
print(second_method)



