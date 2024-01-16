#Question one 
def quotient(input1, input2):
    try: 
        result = input1 / input2
        return result
    except ZeroDivisionError:
        print("Please enter the number bigger than zero")
        return None

result = quotient(12,0)
if result is not None:
    print("Quotient: ",result)

#Question two

try: 
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file 'example.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}.")

#Question three
def listInt(*list):
    try:
        return list[int(input("Enter the index: "))]
    except IndexError:
        print("Enter the right index")
        return None
    except TypeError:
        print("Please enter the right input")
        return None

my_list = [1,2,3,5]
result = listInt(*my_list)

if result is not None:
    print("Result: ",result)