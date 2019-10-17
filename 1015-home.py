key = int(input('enter the key:'))
p = "Be sure to drink your Ovaltine!"
# p = "Or gifr hc qfvbx mcif Cjnyhvbr!"

print(type(p))
c = ""
for i in p:
    if 65 <= ord(i) <= 90:
        j = ord(i) + key
        if  j > 90:
            j = 64 + j - 90
        c = c + chr(j)

    elif 97 <= ord(i) <= 122:
        j = ord(i) + key
        if j > 122:
            j = 96 + j - 122
        c = c + chr(j)
    else:
        c = c + i

print(p)
print(c)

