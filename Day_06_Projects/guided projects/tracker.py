## This is my first guided project using logic from previous days
from grade_model import Grade

# Variable to control the while loop
add_student = True

while add_student:
    action = input("Type 'add' to input a student, or 'quit' to exit: ")

    if action == "add":
        # Getting information from the user
        student_name = input("Enter student name: ")
        score = input("Enter his score: ")

        # Creating an object using our Class from grade_model.py
        new_grade = Grade(student_name, score)

        # Opening the file in 'a' (append) mode so we don't delete old data
        file = open("grades.txt", "a")

        # Writing the object data to the file as a string
        file.write("The student named " + new_grade.student_name + " got a grade of " + str(new_grade.score) + "\n")

        # Always close the file to save memory
        file.close()
        print("Student name and mark saved successfully!")

    elif action == "quit":
        # Change the loop variable to False to stop the program
        add_student = False
        print("Goodbye!")

    else:
        # Handling typos or wrong commands
        print("I don't understand that command.")