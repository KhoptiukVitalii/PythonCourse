name = (input('Введіть Ваше Прізвище Імя Побатькові: '))
print(name)
nameI = name.title()
nameI = nameI.split()
print(nameI)
for i in range(len(nameI)):
    n = nameI[i]
    print(n[0], end="")

