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
    "3": "Three ",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

# Emoji mapping


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊", # fro Emoji Win key + ; together
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(emoji_converter(input(">")))
