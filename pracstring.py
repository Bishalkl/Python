
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


#practise five
message = str(input("Enter a sentence only: "))
list_message = message.split()
count = 0
for i in list_message:
    count+= 1
    
print(count)

#practise six
name_list = ["John","Alice","Bob"]
formatted_message = f"{name_list[0]}, {name_list[1]} and {name_list[2]}."
print(formatted_message)

#practise seven
def countSubstring(mainString, subString):
    count = 0
    mainString = mainString.lower()
    subString = subString.lower()
    mainString_list = mainString.split()
    for i in mainString_list:
        if(subString == i):
            count += 1
    return count

print(countSubstring("Bishal is my name You can call me bishal and so my name is bishal koirala by the way my name is bishal too and bishal and bishal","bishal"))




