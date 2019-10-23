bord = [1]
print(bord)

l = [3,5,-10]
bord.extend(l)
print(bord)

bord_l = len(bord)
print(bord_l)

print(bord.index(3))

index_5 = bord.index(5)
print(bord[index_5 - 1], bord[index_5 + 1])
print(11111)

for i in range(len(bord)):
    print(bord[i], i % 2,  end=" ")
    if i % 2!=0:
        print()

# print(bord)
# index_10 = bord.index(-10)
# bord.pop([-10])
# bord.pop([5])
# bord.insert(index_10, 5)
# bord.insert(index_5, -10)
# print(bord)

bord_l = len(bord)

bord_1 = bord[bord_l - 1]
print(bord_1)
bord[bord_l - 1] = bord[bord_l - 2]
bord[bord_l - 2] = bord_1
print(bord)

index_1 = bord.index(5)
index_2 = bord.index(-10)
print(index_1, index_2)
temp = bord[index_1]
bord[index_1] = bord[index_2]
bord[index_2] = bord[index_1]
print(bord)

bord[index_1], bord[index_2] = bord[index_2], bord[index_1]

ll = [i for i in range(10)]
print(ll)





