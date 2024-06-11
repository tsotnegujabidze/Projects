message = input('Whats up?>')
words = message.split(' ')
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
