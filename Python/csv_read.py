import csv

with open("sales.csv", "r") as file:
     reader = csv.reader(file)

     next(reader)
# → takes/skips the first row
# for row in reader → continues from the second row 
     
     total_sales = 0
     for row in reader:
#         print(row)
#         print(row[0])
#         print(row[1])
#         print(row[2])
        sales = int(row[2])
        print(row[0], row[1], row[2])
        total_sales = total_sales + sales
        if sales > 3000:
           print(row[0], "has high value")

     print("Total sales:",total_sales) 
