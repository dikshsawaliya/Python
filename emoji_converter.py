message = input("Your Message: ")
words = message.split(' ')
emoji_coverter = {
    ":)": "😁",
    ":(": "😔",
    ":/": "😐"
}
output = ""
for word in words:
    output += emoji_coverter.get(word, word) + " "
print(output)