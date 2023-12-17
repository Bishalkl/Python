def greet(first_name, last_name ):
    print(f"Hi,{first_name} {last_name}.")
    print(f"Thank you for coming {first_name}.")


greet("Bishal", "Koirala")

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Bishal_koirala")
print(message)

def collection(*numbers):
    print(numbers)

collection("Bishal", 1, 4, 5, 5)

def even(num):
    if(num % 2 == 0):
        print("It is even number")
    else:
        print("It is not.")

even(10)

#using single arg for get a value only in tuple format
def collection_product(*number):
    total = 1
    for i in number:
        total *= i
    print(f"Here is your total product: {total}")


collection_product(1,2,3,4,)

#using double args for get a keyword with value like a dict
def save_user(**user):
    print(f"this is your detail {user['first_name']}")

save_user(id=1, first_name="Bishal", last_name="Koirala")

#global keyword use for function as local variable in function 
message = "a"
def a():
    global message
    message = "b"

print(message)

#Anonymous Function(Lambda Functions):
multiply = lambda x,y: x*y
print(multiply(1,2))

#Recursion
def evennums(input):
    if input == 2:
        return input
    elif input % 2 != 0:
        return "please enter  even number."
    else:
        return evennums(input - 1)

print(evennums(6)) 

