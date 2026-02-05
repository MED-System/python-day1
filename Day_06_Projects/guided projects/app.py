from book import Book

# This keeps the program running until the user wants to quit
running = True

while running:
    action = input("Type 'add' to save a book, or 'quit' to exit: ")

    if action == "add":
        title = input("Enter book title: ")
        author = input("Enter author: ")

        # Create the object
        new_book = Book(title, author)

        # Save it to a file 
        # We use + to put the strings together exactly like you know
        file = open("library.txt", "a")
        file.write(new_book.title + " by " + new_book.author + "\n")
        file.close()

        print("Book saved successfully!")

    elif action == "quit":
        running = False
        print("Goodbye!")
    else:
        print("I don't understand that command.")