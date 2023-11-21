
list = [10,20,30,40,50]
sum = 0
for i in list:
    sum = sum + i
print(sum)


name = input("Enter your name: ")
sum = 0
for i in range(len(name)):
    asc = ord(name[i])
    sum = sum + asc
print(sum)

name = "shawon"
for i in name:
    print(i, "ascii value is ", ord(i))

list = ["Hello", "World", "Python", "Programmar"]
sum = 0
for i in list:
    sum = sum + len(i)
print(sum)
