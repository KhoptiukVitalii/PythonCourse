tt = 12, "hello", 32
print(tt)
print(type(tt))
print(id(tt))

var = tt[0]
print(var)
x, y, z = tt
print(x, y, z)

# tt[0] = 25
# print(tt)

var1 = ("Hi")*4
print(var1)
var2 = ("Hi",)*4
print(var2)

for i in tt:
    print(i)

tt = (i for i in range(2,11, 3))

tt = (2, 5, 8)
for num, i in enumerate(tt):
    print(num, "-th ->", i)
mm = min(tt)
maxx = max(tt)
ss = sum(tt)
print(mm, maxx, ss)

tt1 = ("cake", "coockies", "apple")
tt2 = (25, 1.2, 12)
tt3 = ["i-f", "lviv", "kyiv"]

for first, second, last in zip(tt1, tt2, tt3):
    print(f"{first} cost {second}$ in {last} city.")

print(type(tt1))
tt1 = list(tt1)
print(type(tt1))
tt1[0] = 12

print(tt1, type(tt1))

tt = ((1,2), (2,4), (6,7))
print(tt)
print(tt[0])

print(tt[2] [0])

for x, y in tt:
    print(x, y)
