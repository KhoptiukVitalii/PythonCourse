ll = [2, 25]
print(ll)

ll.append(45)
print(ll)

ll.extend([32, 67, 89])
print(ll)

# ll.append([32, 67, 89])
# print(ll)

position = ll.index(32)
print(32, ' plased in ', position, '-th position', sep="")
print(f'{32} plased in {position}-th position')

# ll.remove(25)
# ll.remove(5) error
print(ll)
print(ll.remove(25))

item = ll.pop(0)
print(item)
print(ll)
print(f"The lenght of the list is {len(ll)} items.")

ll.reverse()
print(ll)

ll.sort()
print(ll)



