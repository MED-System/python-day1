from inventory_models import Medicine
from validation_tools import eror_handle

stock = []

# Ask how many items we are going to add today
total = int(eror_handle("How many medicines to register? "))
# Start adding each medicine one by one
for i in range(total):
    print(f"\n[Entry {i + 1} of {total}]")
    name = input("Please enter medicine name: ")
    quantity = eror_handle(f"How many units of {name} are in stock? ")

    medicine = Medicine(name, quantity)
    stock.append(medicine)


# Open the file and add our new items
with open("pharmacy_stock.txt", "a") as file:
    for m in stock:
        data_row = m.name + "," + str(m.quantity) + "\n"
        file.write(data_row)

print("Items saved to 'pharmacy_stock.txt'.")
