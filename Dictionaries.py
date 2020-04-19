# Dictionary
customer = {
    "name": "John Smith",
    "age": 36,
    "is_verified": True
}
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"
customer["name"] = "Anupom Roy"
print(customer.get("name"))

# digits mapping
phone = input(" Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch) + " "
print(output)

