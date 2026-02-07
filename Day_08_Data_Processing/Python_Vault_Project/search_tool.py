target = input("What are you looking for? ")
found = False

with open("vault.txt", "r") as search:
    secret = search.readlines()
    for line in secret:
        parts = line.strip().split(":")
        if parts[0] == target:
            print("Found it! Password is: " + parts[1])
            found = True
            break

if not found:
    print("Service not found in the vault.")