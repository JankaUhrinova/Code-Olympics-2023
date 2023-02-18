alphabet = {
    'a': '10',
    'b': '0111',
    'c': '0101',
    'd': '011',
    'e': '1',
    'f': '1101',
    'g': '001',
    'h': '1111',
    'i': '11',
    'j': '1000',
    'k': '010',
    'l': '1011',
    'm': '00',
    'n': '01',
    'o': '000',
    'p': '1001',
    'q': '0010',
    'r': '101',
    's': '111',
    't': '0',
    'u': '110',
    'v': '1110',
    'w': '100',
    'x': '0110',
    'y': '0100',
    'z': '0011',
    '0': '00000',
    '1': '10000',
    '2': '11000',
    '3': '11100',
    '4': '11110',
    '5': '11111',
    '6': '01111',
    '7': '00111',
    '8': '00011',
    '9': '00001',
}

message = input().strip()
#print(message)
result = ""
word = ""
for c in message:
    if c == " ":
        if word == "":
            result += " "
        else:     
            for key, value in alphabet.items():
                if value == word:
                    result += key
            word = ""
    else:
        word += c

for key, value in alphabet.items():
    if value == word:
        result += key

print(result.upper())