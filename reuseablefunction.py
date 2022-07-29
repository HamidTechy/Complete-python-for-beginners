def emojhi_converted(message):
    words = message.split(' ')
    emojhi = {
        ":)": "nahi mila",
        ":(": "ye be nahi"
    }
    output = ""
    for word in words:
        output += emojhi.get(word, word) + " "
    return output


message = input(">")
print(emojhi_converted(message))