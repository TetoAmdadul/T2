sales = [500, 1200, 750, 1800, 950, 2200]
#Print all sales values
print(sales)
#Calculate and print total sales
print("Total sales:",sum(sales))
#Print the highest sale
print(f"Highest sale of the day: {max(sales)}")
#Print the lowest sale
print(f"Todays lowest sale is: {min(sales):.2f}")
#avg
avg_sales = sum(sales)/len(sales)
print(f"The avg is: {avg_sales:.2f}")
#Count how many sales are greater than 1000
count = 0
for sale in sales:
   if sale > 1000:
      count = count + 1

print("Total sales which is over 1000:",count)
#If total sales are 5000 or more, print Target achieved
total_sales = sum(sales)
if total_sales >= 5000:
   print("Target achieved")
else:
   print("Target not achieved")
#append new value
sales.append(7000)
sales[3] = 570
#remove
sales.remove(750)
total_sales = sum(sales)
print(sales[3])
#Print money values with 2 decimal places
print(round(total_sales, 2))

