message = input(">")
words = message.split(' ')
emojhi = {
    ":)": "nahi mila",
    ":(": "ye be nahi"
}
output = ""
for word in words:
   output += emojhi.get(word, word) + " "
print(output)