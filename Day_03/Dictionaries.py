# Creating a dictionary to map short month names to full names
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# Using .get() is safer because it can provide a default value if the key isn't found
print(month_conversions.get("Nov", "Not a valid Key"))