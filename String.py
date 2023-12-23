#Creating Strings:
message1 = 'Hello, World'
message2 = "Bishal"
message3 = """Hi, My name is bishal koiraala.
 I am 20 years world."""

#Concatenation:
a = "Bishal "
b = "koirala"
c = a + b
print(c)

#String Length
myString = "bishal koirala"
print(len(myString)) # len is built in fuction to get a length of string.

#Indexing and Slicing:
first_index = myString[0:1] #first string "B"
print(first_index)

reversedString = myString[::-1] #To reverse the string 
print(reversedString)

#String Methods:
print(myString.upper()) #It will make all the character in uppercase.
print(myString.lower()) #It will make all the character in lowercase.
print(myString.replace("B", "k")) #It will make replace character according to the coder choice.
print(myString.strip('')) #It will remove uneccesary space or character.
print(myString.split()) #It will split the string according to the character.
print(myString.title()) #It will make first character to uppper case of all the word
print(myString.find("o")) #It will find the character and return the index location of character
print("koi" in myString) #it will check character if there is then it will return boolean result whether it is true or false
print("komal" is not myString) # It will also check but it will return false if it is true.

#Formatting
name = "Bishal"
age = 21
address = "Khorsane"
print(f"My name is {name}. I am {age} old. I live in {address}.") #It is really helpful and userfriendly method to Concatenation the multiple String or and other value in formatted way.

#Escape Character
#\n
#\\
#\'
#\"
print("My name is \"bishal\".\nHis name is \'Bishnu limbu\'.")



