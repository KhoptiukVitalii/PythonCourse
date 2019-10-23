weekdays = []
print(weekdays)
weekdays = ['Monday', 'Tuesday', 'weednesday']
print(weekdays)

# first item in the list
print(weekdays[0])

# slice
print(weekdays[0:2])

another_list = list()
print(another_list)

# iterate by string
ll1 = list('cat')
print(ll1)

ll2 = ['cat']
print(ll2)

ll3 = ['cat' , 'dog']
print(ll3)

# error
# ll4 = list('cat', 'dog')
# print(ll4)

ll5 = list(('cat' 'dog'))
print(ll5)

# magic
ll6 = list(('cat', 'dog'))
print(ll6)

ll7 = ['spam', 'eggs', 100, 12.5]
for item in ll7:
    print(item, type(item))
print

# todo -- edit follow loop to print only ==>>
for n, item in enumerate(ll7):
    print(n, item, type(item))


ll8 = ll7 + ["hello"]
print(ll8)
ll9 = ll8 * 3
print(ll9)