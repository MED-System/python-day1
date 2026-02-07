result = input("Enter student name: ")
found = False

with open("grades.txt", "r") as search:
    find = search.readlines()
    for line in find:
         target = line.split(":")
         if target[0] == result:
            print(f"Target found! Grade is: {target[1]}")
            found = True
            break
if not found:
    print("student not found")