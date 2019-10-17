# import string

letters = input("Text to code> ")
key = 10  # secret code

for i in range(len(letters)):
    letter = letters[i]

    # print(letter)

    code = ord(letter)
    newCode = ord(letter) + key
    if 97 <= code <= 122:
        if newCode > 122:
            newCode = newCode - 26
    elif 65 <= code <= 90:
        if newCode > 90:
            newCode = newCode - 26
    else:
        newCode = code

    newLetter = chr(newCode)
    # print(newCode)
    print(newLetter, end="")
