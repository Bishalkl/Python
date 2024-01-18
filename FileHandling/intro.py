#Demo
#write a data
age = input("Enter Your age: ")
f = open("student.txt",'w')
f.write(age)
f.close()

#read
f = open("student.txt",'r')
print(f.read())
f.close()