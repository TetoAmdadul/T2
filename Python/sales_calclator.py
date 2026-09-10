product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
tax_rate = 0.24
subtotal = price * quantity
if subtotal >= 1500:
   discount = subtotal * 0.10
else:
   discount = 0

discounted_subtotal = subtotal - discount
tax = discounted_subtotal * tax_rate
total = discounted_subtotal + tax

print("Product name: ", product)
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Discount_subtotal: {discounted_subtotal:.2f}")
print("Total: ", round(total, 2))
