import csv

with open("sales.csv", "r") as file:
     reader = csv.DictReader(file)
     
     total_sales = 0
     count = 0
     
     highest_sale = 0
     lowest_sale = 0
  
     for row in reader:
         sale = int(row["sales"])
         total_sales = total_sales + sale
         
         if sale > highest_sale:
            highest_sale = sale
        
         count = count + 1
 
         if count == 1:
            lowest_sale = sale
         elif sale < lowest_sale:
           lowest_sale = sale

         print("Customer name is:", row["name"])
                 
     
     average_sales = total_sales / count
     print("Total sales is:", total_sales)
     print(f"Average sales is: {average_sales:.2f}")
     print(f"Highest sale is {highest_sale}")
     print(f"Lowest sale is {lowest_sale}")


