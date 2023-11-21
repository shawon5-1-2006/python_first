x = 10
y = 20
if x == y:
    print("a equal b")
else:
    print("a not equal b")


total_price = 501
discount = 5
if(total_price > 500):
    total_price = total_price -((total_price * discount) / 100)
    print(total_price)
else:
    print(total_price)


age = 19
if(age <= 18):
    print("You are not able to regiter for")
else:
    print("You are eligible")


name = input("Enter your name: ")
size_name = len(name)
if(size_name == 0):
    print("The field can not be empty")
else:
    print("success")


number = input("Enter your number: ")
size_name = len(number)
if(size_name == 11):
    print(" success")
else:
    print("the phone number must be with")