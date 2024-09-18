"""
TASK 2
 Design a simple calculator using python with basic arthmetic operations.
 Prompt the user to input two numbers and an operation choice.
 Perform the calculation and display the result.

 """
def simple_calculator():
    print("...Simple Calculator!...")
    
    # Prompt the user to input two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("\nChoose an operation:")
    print("1 for Addition (+)")
    print("2 for Subtraction (-)")
    print("3 for Multiplication (*)")
    print("4 for Division (/)")
    
    # Get the user's choice
    choice = input("Enter the number corresponding to the operation: ")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = number1 + number2
        operation = "+"
    elif choice == '2':
        result = number1 - number2
        operation = "-"
    elif choice == '3':
        result = number1 * number2
        operation = "*"
    elif choice == '4':
        if number2 != 0:
            result = number1 / number2
            operation = "/"
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Invalid operation choice. Please try again.")
        return
    
    # Display the result
    print(f"\nThe result of {number1} {operation} {number2} is: {result}")

# Run the calculator
simple_calculator()