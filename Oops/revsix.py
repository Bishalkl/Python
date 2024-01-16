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


