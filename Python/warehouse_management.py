products = [
      {"product_name": "Laptop", "price": 2000, "quantity": 10},
      {"product_name": "Mouse", "price": 20, "quantity": 10},
      {"product_name": "Keyboard", "price": 200, "quantity": 2}, 
      {"product_name": "Ram", "price": 250, "quantity": 5},
      {"product_name": "SSD", "price": 400, "quantity": 10},
      {"product_name": "Monitor", "price": 300, "quantity": 90}, 
]

total_inventory_value = 0

for item in products:
    result = item["price"] * item["quantity"]
    total_inventory_value = total_inventory_value + result
    print(item["product_name"], result)

print("Total inventory value in the warehouse is:",total_inventory_value)

for item in products:
    if item["quantity"] <= 5:
       print(item["product_name"], "is low in stock")

low_stock = 0
for item in products:
    if item["quantity"] <= 5:
       low_stock = low_stock + 1

print("Number of low-stock product is:",low_stock)


def calculate_inventory(price, quantity):
    result = price * quantity
    return result

#one dictionary from the dictionaries list

inventory_value = calculate_inventory(products[0]["price"], products[0]["quantity"])
print(inventory_value) 

#Every dictionaries in the list
for item in products:
    inventory_value = calculate_inventory(
        item["price"],
        item["quantity"]
    )
    print(item["product_name"], inventory_value)



