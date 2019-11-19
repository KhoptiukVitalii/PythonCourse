import string

def cesar(key, phrase):
    ''' функція декодуваня слів '''
    str_arr = string.ascii_lowercase
    str_arr2 = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    str_arr += string.ascii_uppercase
    str_arr2 += string.ascii_uppercase[key:] + string.ascii_uppercase[:key]

    cliper_dict= {}
    for k, v in zip(str_arr, str_arr2):
        cliper_dict[k] = v
    ss = ""
    for letter in phrase:
        if letter in cliper_dict:
            ss += cliper_dict[letter]
        else:
            ss += letter
    return ss


with open('story.txt', 'r') as ff: # зчитуємо закодований текст
    text = ff.read()

with open('words.txt', 'r') as eng_dict: # зчитуємо словник англійських слів
    words_eng = eng_dict.read()

# опрацьовуємо текст
text = text.strip()
for symbol in string.punctuation:
    text = text.replace(symbol, "")
words = text.split()
print(text)
print(words)
# декодування слів діапазоном ключів і підрахунок цінності ключа
dict_keys={}
for key in range(1, 27):
    key_value = 0
    for word in words:
        if cesar(key, word) in words_eng:
            key_value += 1
    dict_keys[key] = int(key_value/len(words)*100)# + "%"
    # dict_keys[key] = key_value
print(dict_keys)
# робота оптимального ключа
key_value_max = max(dict_keys.items(), key=lambda item: item[1])
print(key_value_max)
decoded_text = ""
for word in words:
    decoded_text += cesar(key_value_max[0], word) + " "

print(f"ключ {key_value_max[0]}, цінність {key_value_max[1]}%")
print(decoded_text)