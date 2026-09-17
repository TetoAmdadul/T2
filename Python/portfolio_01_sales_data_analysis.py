import csv

def average_sales(total_sales, number_of_sellers):
             average = total_sales / number_of_sellers
             return average


with open("sales.csv", "r") as file:
     reader = csv.DictReader(file)
     
     sales = []
     for row in reader:
         sale = int(row["sales"])
         sales.append(sale)
         
         
         if sale == min(sales):
            lowest_seller = row["name"]
        
         
         if sale == max(sales):
            highest_seller = row["name"]
          
     total = sum(sales)
     sellers = len(sales)   
     lowest_sale = min(sales)
     highest_sale = max(sales)    
     
     count = 0 
     for sale in sales:
         if sale > 3000:
            count = count + 1       
    

     print("Today's sales:", sales)
     print("Total amount of sales team:", total)
     print(f"Lowest seller is {lowest_seller} and lowest sale is: {lowest_sale}")
     print(f"Highest seller is {highest_seller} and highest sale is: {highest_sale}")
     print("Sales more than 3000:", count)    
     print("Average sale is:", round(average_sales(total, sellers), 2))
     
