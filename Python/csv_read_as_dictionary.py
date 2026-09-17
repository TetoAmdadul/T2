import csv

with open("sales.csv", "r") as file:
     reader  = csv.DictReader(file)
     
     total = 0
     for row in reader:
#         print(row)
         print(row["name"])
         print(row["city"])
         print(row["sales"])
         sale = int(row["sales"])
         total = total + sale
              
      
print(total)
