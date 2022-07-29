number = input("enter digits: ")
digit_mapping = {
    "1": "one",
    "2": "tow",
    "3": "three",
    "4": "four"
}
output = ""
for ch in number:
    output += digit_mapping.get(ch, "!") + " "
print(output)