change = int(input('Скільки здачі необхідно видати?:'))
print('change = ', change)
NumberOfСoins = 0
if change > 25:
    change25 = change // 25
    print('change25 =', change25)
    change = change % 25
    print('change = ', change)
    NumberOfСoins = change25
if change > 10:
    change10 = change // 10
    print('change10 =', change10)
    change = change % 10
    print('change =', change)
    NumberOfСoins = NumberOfСoins + change10
if change > 5:
    change5 = change // 5
    print('change5 =', change5)
    change = change % 5
    print('change =', change)
    NumberOfСoins = NumberOfСoins + change5
if change >= 1:
    change1 = change // 1
    print('change1 =', change1)
    change = change % 1
    print('change =', change)
    NumberOfСoins = NumberOfСoins + change1
print("NumberOfСoins",  NumberOfСoins)