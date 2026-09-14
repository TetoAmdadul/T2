customers = [
    {"name": "Amina", "city": "Helsinki", "orders": [120, 1500, 700]},
    {"name": "Rafi", "city": "Espoo", "orders": [2000, 300, 450]},
    {"name": "Sara", "city": "Vantaa", "orders": [100, 200, 300]},
    {"name": "Nabil", "city": "Helsinki", "orders": [2500, 1200, 800]}
]

def order_value(customer):
    total = 0
    
    for order in customer["orders"]:
        total = total + order

    return total
high_value_cus = 0
for customer in customers:
    total_order = order_value(customer)
    print(customer["name"], total_order)
    if total_order > 2000:
       print(customer["name"], "is a high-value customer")
       high_value_cus = high_value_cus + 1

print("High-value customers:", high_value_cus)
