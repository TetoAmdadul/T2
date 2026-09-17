customers = [
    {"name": "Amina", "orders": [500, 1800, 700]},
    {"name": "Rafi", "orders": [2000, 300, 450]},
    {"name": "Sara", "orders": [100, 200, 300]}
]

for customer in customers:
    def calculate_total(customer):
        total = sum(customer["order"])
        return total

print(total)
