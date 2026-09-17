import csv

with open("sales.csv", "r") as file:
     reader = csv.DictReader(file)
     
     sales = []
     for row in reader:
         sale = int(row["sales"])
         sales.append(sale)
         
     count = 0
     for sale in sales:
         if sale > 3000:
            count = count + 1

     total = sum(sales)
     average = total/ len(sales)
     highest_sale = max(sales)
     lowest_sale = min(sales)
    
     print("Total sales is:", total)
     print("Average sales is:", average)
     print("Highest sales is:", highest_sale)
     print("Lowest sales is:", lowest_sale)     
     print("Customer above 3000:", count)
