customers = [
             {"name": "Teto", "city": "Espoo", "orders": [100, 2000, 3000]},
             {"name": "Fatimah", "city": "Helsinki", "orders": [1300, 2030, 3000]},
             {"name": "Maryam", "city": "Kokkola", "orders": [100, 2020, 3030]},
             {"name": "Mily", "city": "Cumilla", "orders": [100, 210, 990]},
]

#without fuction
"""for customer in customers:
    total = 0
    for order in customer["orders"]:
        total = total + order

    print(customer["name"], total)
"""

#finding the total amount using function
def calculate_total(customer):
    total = 0
    for order in customer["orders"]:
        total = total + order
        print(total)

    return total

for customer in customers:
    total = calculate_total(customer)
    print(customer["name"], total)
