product1_name = "computer"
product2_name = "phone"
product1_name = "laptop"

quantity1 = 10
quantity2 = 20
quantity3 = 12

product1_price = 60000
product2_price = 15000
product3_price = 50000

discount = 10

product1_total = quantity1 * product1_price
product2_total = quantity2 * product2_price
product3_total = quantity3 * product3_price + product3_price

quantity_total = quantity1 + quantity2 + quantity3
total = product1_total + product2_total + product3_total
total_after_price = total - (total * discount)/100

print(quantity_total)
print(total)
print(total_after_price)