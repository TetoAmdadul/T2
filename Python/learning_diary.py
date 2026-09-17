with open("README.md", "r") as file:
    old = file.read()


new = r"""# Extra Practice — Python Classes, Objects & File Handling Recall

## 1. What Did I Learn Today?

Today I learned the fundamentals of Python classes and object-oriented programming.

### Class

A class is a blueprint for creating objects.

```python
class Customer:
    pass
```

A class describes what data an object can have and what actions it can perform.

### Object / Instance

An object, also called an instance, is an actual item created from a class.

```python
customer1 = Customer("Amina", "Helsinki", [500, 1800, 9000])
```

Here:

```text
Customer  → class / blueprint
customer1 → object / instance
```

### Instantiate

To instantiate a class means to create an object from that class.

```python
customer1 = Customer("Amina", "Helsinki", [500, 1800, 9000])
```

### Method

A method is a function defined inside a class and associated with objects of that class.

```python
def total_order_value(self):
    return sum(self.orders)
```

Because this function is inside a class, it is called a method.

### `__init__` Method

`__init__` is pronounced **dunder init**.

It is a special initializer method that runs automatically when a new object is created.

```python
class Customer:
    def __init__(self, name, city, orders):
        self.name = name
        self.city = city
        self.orders = orders
```

Its main purpose is to set the object's starting data.

### `self`

`self` refers to the current object that is using the method.

For example:

```python
customer1.total_order_value()
```

Inside the method:

```python
self.orders
```

refers to:

```python
customer1.orders
```

If `customer2` calls the same method, `self` refers to `customer2`.

### Attribute

An attribute is data stored inside an object.

Examples:

```python
self.name
self.city
self.orders
```

They can later be accessed using dot notation:

```python
customer1.name
customer1.city
customer1.orders
```

### Dictionary vs Class Object Access

Dictionary:

```python
customer["name"]
```

Class object:

```python
customer1.name
```

A dictionary mainly stores structured data.

A class can organize both:

```text
data + related behavior
```

### When to Use a Dictionary

A dictionary is useful when the main goal is storing structured data.

```python
customer = {
    "name": "Amina",
    "city": "Helsinki",
    "orders": [500, 1800, 900]
}
```

Dictionaries are especially useful with:

```text
CSV
JSON
APIs
data analysis
structured records
```

### When to Use a Class

A class is useful when data and related actions or calculations belong together.

For example:

```text
Customer data:
name
city
orders

Customer behavior:
calculate total
calculate average
count large orders
determine status
```

### List of Objects

Several objects can be stored inside a list:

```python
customers = [customer1, customer2, customer3]
```

The objects remain Customer objects.

They can then be processed with a loop:

```python
for customer in customers:
    print(customer.name)
```

This connects to an earlier concept:

```text
List of dictionaries → loop through dictionaries
List of objects      → loop through objects
```

### File Handling Recall

I also recalled how to prepend new content to an existing file.

The process is:

```text
read old content
→ store old content
→ create new content
→ open file in write mode
→ write new content + old content
```

Standard pattern:

```python
with open("README.md", "r") as file:
    old = file.read()

new = r'''NEW CONTENT'''

with open("README.md", "w") as file:
    file.write(new + "\n\n" + old)
```

Key file-handling concepts recalled:

```text
"r"      → read
"w"      → write / replace
"a"      → append
.read()  → read file content
.write() → write content
"\n"     → newline
"\n\n"   → two newlines / one blank line
```

## 2. What Did I Do Today?

I created a Customer class and used methods to analyse customer order data.

My working class was:

```python
class Customer:

    def __init__(self, name, city, orders):
        self.name = name
        self.city = city
        self.orders = orders

    def total_order_value(self):
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
            return self.name + " has High value"
        else:
            return "Customer needs more attention"
```

I created three Customer objects:

```python
customer1 = Customer("Amina", "Helsinki", [500, 1800, 9000])
customer2 = Customer("Rafi", "Espoo", [500, 1800, 1100])
customer3 = Customer("Bob", "Vantaa", [500, 1800, 900])
```

I accessed object attributes:

```python
customer1.name
customer1.city
customer1.orders
```

I called object methods:

```python
customer1.total_order_value()
customer1.calculate_average()
customer1.count_large_orders()
customer1.customer_status()
```

I formatted the average to two decimal places:

```python
print(f"Average is: {customer1.calculate_average():.2f}")
```

I also learned a cleaner way to process all Customer objects instead of repeating the same print statements:

```python
customers = [customer1, customer2, customer3]

for customer in customers:
    print("Customer name:", customer.name)
    print("City:", customer.city)
    print("Total order value:", customer.total_order_value())
    print(f"Average order value: {customer.calculate_average():.2f}")
    print("Large orders:", customer.count_large_orders())
    print("Status:", customer.customer_status())
    print()
```

This is cleaner because the same code works for every Customer object.

I also recalled the README file-handling pattern:

```python
with open("README.md", "r") as file:
    old = file.read()

with open("README.md", "w") as file:
    file.write(new + "\n\n" + old)
```

## 3. Interview Questions & Answers

### What is a class?

A class is a blueprint for creating objects that can contain data and related behavior.

### What is an object?

An object is an actual instance created from a class.

### What does instance mean?

An instance is an object created from a particular class.

### What does instantiate mean?

To instantiate means to create an object from a class.

### What is a method?

A method is a function defined inside a class and associated with objects of that class.

### What is `__init__`?

`__init__`, pronounced dunder init, is a special initializer method that automatically runs when a new object is created and is normally used to set the object's initial data.

### Is `__init__` a function or a method?

Because `__init__` is defined inside a class, it is a method. More specifically, it is a special initializer method.

### Why do we use `self`?

`self` refers to the current object and allows a method to access that object's attributes and other methods.

### What is an attribute?

An attribute is data stored inside an object.

### What is the difference between a dictionary and a class?

A dictionary is mainly used to store structured key-value data. A class can organize both data and related methods or behavior.

### How do I access data in a dictionary?

```python
customer["name"]
```

### How do I access an object's attribute?

```python
customer1.name
```

### Can objects be stored inside a list?

Yes.

```python
customers = [customer1, customer2, customer3]
```

The objects remain instances of their original class.

### Why use a loop for several objects?

A loop avoids repeating the same code for every object.

```python
for customer in customers:
    print(customer.name)
```

### What is the difference between `return` and `print()`?

`return` sends a value back from a function or method.

`print()` displays a value on the screen.

### Why did a method sometimes show `None`?

If a method does not return a value, Python returns `None`.

### Why did a method return a tuple when I used a comma?

This:

```python
return self.name, "has High value"
```

returns two values together as a tuple.

### Why is a class name normally capitalized?

Python convention uses PascalCase for class names.

Examples:

```text
Customer
CustomerOrder
BankAccount
```

Variables and functions normally use lowercase or snake_case.

### When should I use a dictionary?

Use a dictionary when the main goal is storing and accessing structured data.

### When should I use a class?

Use a class when related data and behavior should be organized together.

## 4. Summary — Mistakes & Corrections

### Mistake: Writing `__int__` instead of `__init__`

Incorrect:

```python
def __int__(self, name, city, orders):
```

Correct:

```python
def __init__(self, name, city, orders):
```

`__init__` requires double underscores before and after `init`.

### Mistake: Using `orders` instead of `self.orders`

Incorrect:

```python
for order in orders:
```

Correct:

```python
for order in self.orders:
```

Inside the method, the orders belong to the current object.

### Mistake: Putting `return` inside the loop

Incorrect structure:

```python
for order in self.orders:
    total = total + order
    return total
```

This stops the method after the first iteration.

Correct structure:

```python
for order in self.orders:
    total = total + order

return total
```

### Mistake: Using `avg()`

I tried:

```python
average = avg(orders)
```

Python does not have a built-in `avg()` function.

I corrected the calculation using:

```python
average = sum(self.orders) / len(self.orders)
```

### Mistake: Hard-coding the number of orders

Instead of:

```python
average = total / 3
```

I learned to use:

```python
len(self.orders)
```

so the calculation works with different numbers of orders.

### Mistake: Returning nothing

I used:

```python
return
```

which returned:

```text
None
```

I learned that a method should return an actual value when a result is needed.

### Mistake: Printing inside the method and printing the method again

This caused the message to print followed by:

```text
None
```

I changed the method to return a value and used `print()` outside.

### Mistake: Returning two comma-separated values

This:

```python
return self.name, "has High value"
```

creates a tuple.

For one readable string, I used string concatenation instead.

### Mistake: Repeating customer printing manually

I originally repeated the same print statements for `customer1`, `customer2`, and `customer3`.

A cleaner approach is:

```python
customers = [customer1, customer2, customer3]

for customer in customers:
    print(customer.name)
```

### Mistake: Forgetting that objects can be stored in a list

I understood that a loop could help process all customers, but I did not immediately recall the syntax:

```python
customers = [customer1, customer2, customer3]
```

The important lesson is that putting objects in a list does not change them. They remain Customer objects.

### Main Lessons

```text
Class
→ blueprint

Object / Instance
→ actual object created from the class

Instantiate
→ create an object from a class

__init__
→ special initializer method

self
→ current object

Attribute
→ data stored in an object

Method
→ function defined inside a class

Dictionary
→ mainly structured data

Class
→ related data + behavior

List of objects
→ process several objects with one loop

return
→ send a value back

print()
→ display a value
"""
    

with open("README.md", "w") as file:
    file.write(new + "\n\n" + old)
