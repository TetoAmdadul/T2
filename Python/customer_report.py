import csv

with open("customer_report.csv", "w") as file:
     
     writer = csv.writer(file)
    
     writer.writerow(["name", "city", "sales"])
     writer.writerow(["Amina", "Helsinki", 3200])
     writer.writerow(["Rafi", "Espoo", 1400])
     writer.writerow(["Bob", "Vantaa", 4300])
