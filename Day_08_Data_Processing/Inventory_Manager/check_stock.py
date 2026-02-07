while True:
    # Get name of item needed
    target = input("What are you looking for? (or type 'exit' to stop program): ")

    # Check if they want to stop the program
    if target.lower() == "exit":
        print("Goodbye! 👋")
        break

    # Record if we found a match
    found = False

    # Open the file to read it
    with open("inventory.txt", "r") as fruits:
        # Read every line into a list
        stock = fruits.readlines()
        # Go through each line one by one
        for line in stock:
            parts = line.strip().split(":")

            # Compare names ignoring capital letters
            if parts[0].lower() == target.lower():
                found = True
                # Turn the text into a number
                quantity = int(parts[1])

                # Check if number is higher than zero
                if quantity > 0:
                    print(f"Found it! We have {quantity} in stock.")
                else:
                    print("Out of stock.")
                break

    # If loop finished and found is still False
    if not found:
        print("Item not available in inventory.")