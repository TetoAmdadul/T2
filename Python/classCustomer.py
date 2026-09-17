class CustomerOrder:
      def __init__(self, product, price, quantity):
          self.product = product
          self.price = price
          self.quantity = quantity
          self.result = None
  
      def total_order(self):
          self.result = self.price * self.quantity
          return self.result


mika = CustomerOrder("Laptop", 900, 3)

print(mika.total_order())
