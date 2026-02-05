from converter_logic import CurrencyConverter

# 1. Create the converter object (The "Tool")
my_tool = CurrencyConverter()

# 2. Get the amount and turn it into a float (decimal number)
amount = float(input("How many dollars do you have? "))

# 3. Ask for the currency
action = input("Which currency (EUR, GBP, or JPY)? ")

result = my_tool.convert(amount, action)

# 5. Check if the result exists and print it
if result != None:
    print("Your converted amount is: " + str(result))
else:
    print("Sorry, we don't support that currency.")
