# Function to find the biggest number
def max_num(num1, num2, num3):
    # Check if num1 is bigger than the others
    if num1 >= num2 and num1 >= num3:
        return num1
    # Check if num2 is bigger than the others
    elif num2 >= num1 and num2 >= num3:
        return num2
    # If neither of those, num3 must be the biggest
    else:
        return num3

print(max_num(300, 40, 5))