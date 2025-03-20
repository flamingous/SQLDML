def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#Create a dictionary 'operations' that assigns the functions to their corresponding operation symbols.
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
# print(operations["+"](2, 3))

# #step:3 Create a function 'calculator' that prompts the user to input the first number.
def calculator():
    should_continue = True
    first_number = float(input("Enter the first number: "))
    #Use a for loop to print the available operation symbols.
    print("These are the available operations")
    for operation_symbol in operations.keys():
        print(operation_symbol)

    while should_continue:
        #inside the while loop, prompt the user to select an operation symbol
        operation_symbol = input("Pick an operation: ")
        #if the operation symbol is not in the operations dictionary, print an error
        #message and continue to the next iteration of the loop
        if operation_symbol not in operations:
            print("Invalid operation")
            continue #continue to the next iteration of the loop
        else:
            #prompt the user to input the second number
            second_number = float(input("Enter the second number: "))

            #if the operation is in the operations dictionary, assign the 
            #corresponding function to the variable "function_name"
            calculation_function = operations[operation_symbol]

            #Perform the calculation by calling the 'calculation_function' on the two input numbers 
            #and store the result in a variable 'answer'.
            answer = calculation_function(first_number, second_number)
            #Print the equation and the result of the calculation.
            print(f"{first_number} {operation_symbol} {second_number} = {answer}")

            #Ask the user if they would like to continue using the result 
            # as the first number for further calculations.
            choice = input("Do you want to continue with the result as the first number? type 'yes' or 'no': ")
            if choice == "yes":
                first_number = answer
            elif choice == "no":
                should_continue = False
                calculator()
            elif choice == "stop":
                print("Thank you for using the calculator")
                break
            else:
                print("Invalid choice. The choices are yes or no and stop")
                

calculator()
