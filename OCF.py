a  = 11 / 4 # give all the value largest and smallest or decimal number.
b = 11 // 4 #only give the largest value.
c = 2 ** 3 #this give the power of the value you give or exponentiation
print(a,b,c)

d = 2
e = 1
if d or e == 2:
    print(True)
else: 
    print(False)

f = 12
g = 12
h = f is not g 
print(h)


character = ['a', 'b,', 'c', 2, 3]
is_arrays = 2 in character
is_arrays1 = 'a' in character
is_arrays2 = 'Bishal' in character
print(is_arrays, is_arrays1, is_arrays2)


num = 12
if(num % 2 == 0):
    print(str(num) + " is even number!")
elif(num == 0):
    print(str(num) + " is 0!")
else:
    print(str(num) + " is odd number!")

# this is for loop
fruits = [1,2,3,4,5,6,7,8,9,10]
for even in fruits:
    if even % 2 == 0:
        print(str(even) + '\n')

# this is while loop
count = 0
while count < 10:
    if count % 2 != 0:
        print(str(count) + '\n') # str is string format to add different data type 
    count+=1

# exepction handeling 
a = 12
b = 12

try:  # risky code 
    c = a / b
    print(c)

except: #back up for try 
    print("the value you give is not applicable")

finally: # it will run even in both condition 
    print("it always execute ")
    
print("Hello world ")

if(23 % 2 == 0):
    print("Even number")
else:
    print("Odd Number")
    

