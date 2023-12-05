list_1= [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

list_1.insert(2, [9,0,1,2])
list_1.insert (3, [3,4,5,6])
list_1.pop(4)
list_1.pop(-1)
print(list_1)

even_numbers_list =[]
odd_numbers_list = []

for list in list_1:
    even_numbers = [num for num in list if num %2==0]
    odd_numbers = [num for num in list if num %2 !=0]

    even_numbers_list.append( even_numbers)
    odd_numbers_list.append( odd_numbers)

print("even numbers list:",even_numbers_list)
print("odd_numbers_list:",odd_numbers_list)

sums_list = [sum(list) for list in list_1]

print(sums_list)