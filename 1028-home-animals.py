animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'hiena'

print(animals)

animals_len = len(animals)
print(animals_len)

if "c" in animals:
    print("c:", animals['c'])
else:
    print('setpoint not found')
if 'e' in animals:
    print("e:", animals['e'])
else:
    print('setpoint not found')

for i,j in enumerate(animals):
    print(f"{i}) {j} = ", end="")
    print(animals[j])


