import string

#
# text = input("Enter The Text>>")
# text = text.lower()
# text_half = len(text) // 2
# for i in range(text_half):
#     if text[i] != text[len(text)-1-i]:
#         break
#     elif i != text_half - 1:
#         continue
#     print("The text you enter is a polyndrome")


text = input("Enter The Text>>")
text = text.lower()
text_only = ""
for i in text:
    if i.isalpha():
        text_only = text_only + i

text_half = len(text_only) // 2

for i in range(text_half):
    if text_only[i] != text_only[-i-1]:
        break
    elif i != text_half - 1:
        continue
    print("The text you enter is a polyndrome")
