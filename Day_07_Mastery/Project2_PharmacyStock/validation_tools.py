def eror_handle(prompt):

    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Must be a positive integer.")
            else:
                return value
        except ValueError:
            print("Error: value entered Must be an integer.")
