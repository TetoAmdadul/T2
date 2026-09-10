order_amount = float(input("Enter total amount: "))
distance = float(input("Enter distance in km: "))

if order_amount >= 1000:
   delivery_charge = 0
elif distance <= 5:
     delivery_charge = 50
else:
     delivery_charge = 100

total = order_amount + delivery_charge

print("Your order amount is:",order_amount,f" and your delivery charge is:{delivery_charge:.2f}",". So Your Final amount is:",round(total,2))
#print(f"Delivery charge will be : {delivery_charge:.2f}")
#print("Your total amount is: ", round(total,2))

