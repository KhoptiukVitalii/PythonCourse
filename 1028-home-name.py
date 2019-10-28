name = ['Vova', 'Valja', 'Petro', 'Ivan']
age = [1990, 2000, 1995, 2002]

dict = {}

for i in range(len(name)):
    dict[name[i]] = age[i]
print(dict)

print(sorted(dict))

years_sorted = sorted(dict.values())
print(sorted(dict.values()))

for year in years_sorted:
    for i,j in dict.items():
        if j == year:
            print(i, ":", j)