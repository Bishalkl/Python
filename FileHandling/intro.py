#Demo

#write a data
age = input("Enter Your age: ")
f = open("student.txt",'w')
f.write(age)
f.close()

#read a data
f = open("student.txt",'r')
print(f.read())
f.close()

#firstly open

#Opening files:
#f = open(filename,mode="r", buffering, encoding=None, errors=None,newline=None, colsfd=True)
#r mode is for reading

#Open file
f = open('/home/bishal/Desktop/Personal/Python/TXT.txt',mode='w')

if f:
    print("Successfuly Opened")
print(type(f))

#Open function Arguments

#Buffering: it is a speend of transfor how much you want to run

#encoding: it has unique character of system

#errors: Represents how encoding and decoding errors are to be handled. Cannot be used in binary mode. Some standard value are: strict, ignore, replace etc.

#newline: \n,\r,\r\n.

#Buffering, encoding 
g = open('student.txt', mode='r',buffering=10, encoding='utf-8')
if g:
    print("Opened")
print(type(g))

