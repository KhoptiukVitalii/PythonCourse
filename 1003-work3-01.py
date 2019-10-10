# for i in range(1, 11, 2):
#   print(i)

# height = int(input("Enter height> "))
# for i in range(height):
#    for k in range(i + 1):
#        print("#", end="")
#    print()

# height = int(input("Enter height> "))
# for i in range(height):
#     for k in range(i + 1):
#         print("#", end="")
#     print()

height = int(input("Enter height> "))
for up in range(height):
    print(" ", end="")
print("*")
for i in range(height):
    for z in range(height-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print (" ", end="")
    for x in range(i+1):
        print("*", end="")
    print( )

# print('Добрий', end=" ")
# print('День', end=" ")
# print('дорогі', end=" ")
# print('друзі', end=" ")


