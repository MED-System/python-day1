# Convert user input from strings to floats for mathematical operations
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Flow control: check the operator to determine the math operation
if op == "+":
    #  addition
    print(num1 + num2)
elif op == "-":
    #  subtraction
    print(num1 - num2)
elif op == "/":
    #  division
    print(num1 / num2)
elif op == "*":
    #  multiplication
    print(num1 * num2)
else:
    # Fallback if no valid operator is detected
    print("Invalid Operator")