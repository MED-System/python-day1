from employee import Employee
from developer import Developer

action = input("Add Employee or Developer? ")

if action == "Employee":
    # 1. Get the data
    name_input = input("Enter employee name: ")
    id_input = input("Enter ID number: ")

    # 2. Create the object (Use your class 'Employee' here)
    new_emp = Employee(name_input, id_input)

    # 3. Save it
    file = open("staff.txt", "a")
    file.write("Employee: " + new_emp.name + " ID: " + str(new_emp.id_number) + "\n")
    file.close()
    print("Employee saved!")

elif action == "Developer":
    # 1. Get the data (Add the extra language input)
    name_input = input("Enter developer name: ")
    id_input = input("Enter ID number: ")
    lang_input = input("Enter programming language: ")

    # 2. Create the Developer object
    new_dev = Developer(name_input, id_input, lang_input)

    # 3. Save it
    file = open("staff.txt", "a")
    file.write("Dev: " + new_dev.name + " (" + new_dev.language + ")\n")
    file.close()
    print("Developer saved!")