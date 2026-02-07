def eror_handle(prompt):
    while True:
        try:
            #Get input, convert to float, check if > 0
            value = float(input(prompt))
            if value <= 0:
                print("Error: Must be a positive number.")
            else:
                return value # This breaks the loop and sends the data back
        except ValueError:
            print("Error: Invalid input. Please enter a number.")