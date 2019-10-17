import string


# cameCase
# snake_case
def foo_code_cesar(ll, l_key):
    code = ord(ll)
    newCode = ord(ll) + l_key
    if ll in string.ascii_lowercase:
        if newCode > ord("z"):
            newCode = newCode - 26
    elif ll in string.ascii_uppercase:
        if newCode > ord("Z"):
            newCode = newCode - 26
    else:
        newCode = code

    new_ll = chr(newCode)
    return new_ll


letters = input("Text to code> ")
key = int(input("secret key>>"))  # secret code

for letter in letters:
    newLetter = foo_code_cesar(letter, key)
    print(newLetter, end="", flush=True)
