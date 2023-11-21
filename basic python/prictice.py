

name = input("Enter your name: ")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    sum = sum + asc
print(sum)

