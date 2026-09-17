class Customer:
      def __init__(self, name, city, orders):
          self.name = name
          self.city = city
          self.orders = orders
          
      def total_order_value(self):
#          total = 0
#         for order in 	self.orders:
#             total = total + order
#          return total
          return sum(self.orders)
      
      def calculate_average(self):
          average = sum(self.orders) / len(self.orders)
          return average
      
      def count_large_orders(self):
          count = 0
          for order in self.orders:
              if order > 1000:
                 count = count + 1
          
          return count

      def customer_status(self):
          if sum(self.orders) > 3300:
             return(self.name + " has High value")       
          else:
             return "Customer needs more attention"
    
customer1 = Customer("Amina", "Helsinki", [500, 1800,9000])
customer2 = Customer("Rafi", "Espoo", [500, 1800, 1100])
customer3 = Customer("Bob", "vantaa", [500, 1800,900])


if customer1:
    print("Customer name is:", customer1.name)
    print(customer1.name + "'s city is: " + customer1.city)
    print("Total order value is:",customer1.total_order_value())
    print(f"Average is: {customer1.calculate_average():.2f}") 
    print("Number of large order is:", customer1.count_large_orders())
    print(customer1.customer_status())

if customer2:
    print("Customer name is:", customer2.name)
    print(customer2.name + "'s city is: " + customer2.city)
    print("Total order value is:",customer2.total_order_value())
    print(f"Average is: {customer2.calculate_average():.2f}")
    print("Number of large order is:", customer2.count_large_orders())
    print(customer2.customer_status())

if customer3:
    print("Customer name is:", customer3.name)
    print(customer3.name + "'s city is: " + customer3.city)
    print("Total order value is:",customer3.total_order_value())
    print(f"Average is: {customer3.calculate_average():.2f}")
    print("Number of large order is:", customer3.count_large_orders())
    print(customer3.customer_status())

