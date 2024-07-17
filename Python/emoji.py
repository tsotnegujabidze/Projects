message = input('Which emoji would you like to convert>')
words = message.split()
emojis = {
    ':)': '😊',
    ':(': '🙁',
    '-_-': '😑',
    ':0': '😲',
    ';)': '😉',
    ':p': '😝'
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output) 
