# Python Learning & Portfolio Journey

# Day 5 — Nested Data, Nested Loops, Functions & Customer Analysis

## 1. What Did I Learn Today?

I learned:

- Nested data structures
- List of dictionaries
- Lists inside dictionaries
- Nested loops
- Outer loop and inner loop
- Dictionary key access
- `.values()`
- `.items()`
- Key-value unpacking
- Functions with dictionaries
- Accumulators
- Counters
- `return`
- REPL vs `.py` files

### Nested Data Structure

Nested data means one data structure is stored inside another.

```python
customer = {
    "name": "Mika",
    "city": "Espoo",
    "orders": [500, 1800, 700]
}
```

Here:

```python
customer["orders"]
```

returns a list stored inside the dictionary.

### Nested Loop

A nested loop is a loop inside another loop.

```python
for customer in customers:
    for order in customer["orders"]:
        print(order)
```

### `.items()`

`.items()` is used when both dictionary keys and values are needed.

```python
for key, value in customer.items():
    print(key, value)
```

### Accumulator

An accumulator builds a running value.

```python
total = 0
total = total + order
```

### Counter

A counter counts how many times something happens.

```python
high_value_count = 0
high_value_count = high_value_count + 1
```

### `return`

`return` sends a value calculated inside a function back to the caller.

---

## 2. What Did I Do Today?

I created customer data using a list of dictionaries:

```python
customers = [
    {"name": "Amina", "city": "Helsinki", "orders": [120, 1500, 700]},
    {"name": "Rafi", "city": "Espoo", "orders": [2000, 300, 450]},
    {"name": "Sara", "city": "Vantaa", "orders": [100, 200, 300]},
    {"name": "Nabil", "city": "Helsinki", "orders": [2500, 1200, 800]}
]
```

I created a function to calculate one customer's total orders:

```python
def calculate_order_total(customer):
    total = 0

    for order in customer["orders"]:
        total = total + order

    return total
```

Then I processed all customers:

```python
high_value_count = 0

for customer in customers:
    total_order = calculate_order_total(customer)

    print(customer["name"], total_order)

    if total_order > 2000:
        print(customer["name"], "is a high-value customer")
        high_value_count = high_value_count + 1

print("High-value customers:", high_value_count)
```

Output:

```text
Amina 2320
Amina is a high-value customer
Rafi 2750
Rafi is a high-value customer
Sara 600
Nabil 4500
Nabil is a high-value customer
High-value customers: 3
```

I also practised:

```python
print(customer)
print(customer["name"])
print(customer.values())
print(customer.items())
```

---

## 3. Interview Questions & Answers

### What is a nested data structure?

A nested data structure is a data structure stored inside another data structure.

### What is a nested loop?

A nested loop is a loop inside another loop.

### What is the difference between `customers` and `customer`?

`customers` represents many customer dictionaries.

`customer` represents one customer dictionary.

### Why does `customers["name"]` not work?

Because `customers` is a list.

A list first needs an integer index:

```python
customers[0]["name"]
```

### When do I use `.items()`?

When I need both the keys and values of a dictionary.

### Can I use `.items()` directly on `customers`?

No. `customers` is a list.

Each `customer` inside it is a dictionary, so:

```python
customer.items()
```

works.

### Where does the function parameter `customer` get its value?

It receives its value when the function is called.

```python
calculate_order_total(customer)
```

### Does a function need two parameters?

No. A function can have zero, one, two, or more parameters.

### Is a one-parameter function a lambda function?

No. A function created using `def` is a normal user-defined function.

### Why do we use `return`?

`return` sends the calculated value from inside the function back outside.

### Why should `return` be outside the order loop?

Because `return` ends the function. If it is inside the loop, the function can stop after the first order.

### Do variables inside and outside a function need the same name?

No.

`return` sends the value, not the variable name.

### What is REPL?

REPL means:

```text
Read
Evaluate
Print
Loop
```

It is Python's interactive `>>>` environment.

### What is the difference between REPL and a `.py` file?

REPL keeps variables while the current session remains active.

A `.py` file runs independently from top to bottom and must contain the data it needs.

---

## 4. Summary — Mistakes & Corrections

### Mistake: Looping over the wrong object

I wrote:

```python
for order in customer:
```

This loops through dictionary keys.

Correction:

```python
for order in customer["orders"]:
```

### Mistake: Comparing a list with an integer

I tried:

```python
if customer["orders"] > 1000:
```

`customer["orders"]` is a whole list.

Correction:

```python
if order > 1000:
```

### Mistake: Using `customers["name"]`

`customers` is a list, not a dictionary.

Correction:

```python
customers[0]["name"]
```

or:

```python
for customer in customers:
    print(customer["name"])
```

### Mistake: Putting `return` inside the loop

This would cause the function to stop too early.

Correction:

```python
for order in customer["orders"]:
    total = total + order

return total
```

### Mistake: Counting high-value customers using the wrong loop

I accidentally looped through the last `customer` dictionary instead of the full `customers` list.

Correction:

Increment the counter inside the main customer loop:

```python
if total_order > 2000:
    high_value_count = high_value_count + 1
```

### Important Lesson

```text
customers
→ many records

customer
→ one record

customer["orders"]
→ nested list

order
→ one value

function
→ calculation logic

return
→ sends calculated value back
```

---

# Day 4 — Functions, Return Values & Scope

## 1. What Did I Learn Today?

I learned:

- User-defined functions
- `def`
- Parameters
- Arguments
- Function calls
- Statements
- Expressions
- `return`
- Local variables
- Scope
- Built-in functions
- Functions combined with loops

### Function

A function is a reusable block of code that performs a task.

```python
def function_name():
    statement
```

### Parameter

A parameter is a variable written in a function definition.

```python
def show_product(product_name):
    print(product_name)
```

### Argument

An argument is an actual value passed into a function.

```python
show_product("Laptop")
```

### Return

```python
return result
```

sends a value back to the caller.

### Scope

Scope determines where a variable can be accessed.

A variable created inside a function is normally a local variable.

---

## 2. What Did I Do Today?

I created functions such as:

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    return result
```

Then called them:

```python
inventory_value = calculate_inventory(2000, 10)
print(inventory_value)
```

I also combined functions with product dictionaries:

```python
for item in products:
    inventory_value = calculate_inventory(
        item["price"],
        item["quantity"]
    )

    print(item["product_name"], inventory_value)
```

---

## 3. Interview Questions & Answers

### What is a function?

A reusable block of code that performs a specific task.

### What is a parameter?

A variable defined in the function header.

### What is an argument?

The actual value passed to the function.

### What is a statement?

An instruction executed by Python.

### What is an expression?

Code that produces a value.

```python
price * quantity
```

### What is the difference between `print()` and `return`?

`print()` displays a value.

`return` sends a value back to the caller.

### What happens if a function does not have `return`?

Python returns:

```python
None
```

### What is a local variable?

A variable created inside a function.

### Does `return` make a local variable global?

No.

It only sends the value outside.

### What is the difference between a function and a loop?

A function organizes reusable logic.

A loop repeats an operation.

---

## 4. Summary — Mistakes & Corrections

### Mistake: Using `print()` when I needed `return`

I created:

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    print(result)
```

The function displayed the result but returned `None`.

Correction:

```python
return result
```

### Mistake: Confusing parameters and arguments

Correction:

```python
def calculate_inventory(price, quantity):
```

`price` and `quantity` are parameters.

```python
calculate_inventory(500, 3)
```

`500` and `3` are arguments.

### Mistake: Confusion about scope

I learned that an inside variable and outside variable can have the same name but still belong to different scopes.

### Important Lesson

```text
Function
→ reusable logic

Parameter
→ placeholder

Argument
→ actual input

return
→ sends result back
```

---

# Day 3 — Dictionaries & Warehouse Analysis

## 1. What Did I Learn Today?

I learned:

- Dictionaries
- Keys
- Values
- Key-value pairs
- Dictionary access
- Updating values
- Adding new keys
- `.items()`
- `.values()`
- Unpacking
- List of dictionaries
- Accumulators
- Counters

### Dictionary

```python
product = {
    "product_name": "Laptop",
    "price": 2000,
    "quantity": 10
}
```

### Access a Value

```python
product["product_name"]
```

### Update a Value

```python
product["quantity"] = 5
```

### `.items()`

```python
for key, value in product.items():
    print(key, value)
```

---

## 2. What Did I Do Today?

I created warehouse/product data:

```python
products = [
    {"product_name": "Laptop", "price": 2000, "quantity": 10},
    {"product_name": "Mouse", "price": 20, "quantity": 10},
    {"product_name": "Keyboard", "price": 200, "quantity": 2}
]
```

I calculated inventory values:

```python
total_inventory_value = 0

for item in products:
    result = item["price"] * item["quantity"]
    total_inventory_value = total_inventory_value + result
```

I identified low-stock products:

```python
for item in products:
    if item["quantity"] <= 5:
        print(item["product_name"], "is low in stock")
```

---

## 3. Interview Questions & Answers

### What is a dictionary?

A data structure that stores key-value pairs.

### What is a key?

A key identifies a value.

### What does `.items()` return?

Key-value pairs.

### What does `.values()` return?

Dictionary values.

### What happens when I loop directly over a dictionary?

Python normally iterates through the keys.

### Why do we initialize an accumulator with `0`?

Because it needs a starting value before values can be added repeatedly.

### What is the difference between `if` and `for`?

`if` makes a decision.

`for` repeats an operation.

### What is a list of dictionaries?

A list containing multiple structured records.

---

## 4. Summary — Mistakes & Corrections

### Mistake: Trying to unpack a dictionary directly

I tried:

```python
for key, value in customer:
```

Correction:

```python
for key, value in customer.items():
```

### Mistake: Calling `.items()` on a list

Correction:

```python
for product in products:
    for key, value in product.items():
        print(key, value)
```

### Mistake: Accumulator initialization confusion

I learned:

```python
total = 0
```

must be created before:

```python
total = total + value
```

### Important Lesson

```text
Dictionary
→ one structured record

List of dictionaries
→ many structured records
```

---

# Day 2 — Lists, Loops & Sales Analysis

## 1. What Did I Learn Today?

I learned:

- Lists
- Indexes
- `for` loops
- `sum()`
- `len()`
- `max()`
- `min()`
- Average calculations
- Counters
- List methods

### List

```python
sales = [1200, 850, 2100, 600]
```

### Index

Indexes start at `0`.

```python
sales[0]
```

### For Loop

```python
for item in collection:
    statement
```

### Counter

```python
count = 0

for sale in sales:
    if sale > 1000:
        count = count + 1
```

---

## 2. What Did I Do Today?

I analysed sales data:

```python
total_sales = sum(sales)
average_sales = total_sales / len(sales)

print(total_sales)
print(average_sales)
print(max(sales))
print(min(sales))
```

I practised list methods:

```python
sales.append(7000)
sales.remove(850)
sales.insert(1, 1000)
sales.pop(2)
```

I also updated values using indexes.

---

## 3. Interview Questions & Answers

### What is a list?

An ordered collection containing multiple values.

### What is an index?

The numerical position of an item in a list.

### What is a `for` loop?

A loop that processes items from a collection one at a time.

### What does `sum()` do?

Adds numerical values.

### What does `len()` do?

Returns the number of items.

### What is a counter?

A variable used to count occurrences.

### What is a method?

A function associated with an object.

Example:

```python
sales.append(500)
```

---

## 4. Summary — Mistakes & Corrections

### Mistake: Confusing indexes and values

I learned:

```python
sales[0]
```

means the first value.

### Mistake: Expecting `.py` scripts to display expressions automatically

Correction:

Use:

```python
print(...)
```

### Mistake: Confusing loop-variable names with indexes

Example:

```python
for item in sales:
```

`item` represents the current value.

### Important Lesson

Lists allow multiple ordered values to be stored and processed using loops.

---

# Day 1 — Python Fundamentals & Business Calculations

## 1. What Did I Learn Today?

I learned:

- Variables
- Strings
- Integers
- Floats
- `input()`
- Type conversion
- Arithmetic calculations
- `if`, `elif`, `else`
- Comparison operators
- f-strings
- `round()`
- Basic debugging

### Variable

```python
price = 100
quantity = 5
```

### Conditional Statement

```python
if subtotal >= 1500:
    print("Discount applied")
else:
    print("No discount")
```

### f-string

```python
print(f"Total: {total:.2f}")
```

---

## 2. What Did I Do Today?

I created a business sales calculator using:

```text
Product
↓
Price
↓
Quantity
↓
Subtotal
↓
Discount
↓
Tax
↓
Final total
```

Example:

```python
subtotal = price * quantity

if subtotal >= 1500:
    discount = subtotal * 0.10
else:
    discount = 0

discounted_subtotal = subtotal - discount
tax = discounted_subtotal * 0.24
total = discounted_subtotal + tax

print(f"Total: {total:.2f}")
```

I also practised delivery conditions and debugging.

---

## 3. Interview Questions & Answers

### What is a variable?

A name used to store a value.

### What is an integer?

A whole number.

### What is a float?

A number containing a decimal part.

### Why do we use `if`?

To make decisions based on conditions.

### Why do we use `int()` or `float()` with `input()`?

Because `input()` returns text, while numerical calculations require numerical data types.

### What is an f-string?

A formatted string that allows variables and expressions to be inserted into text.

### Why can floating-point calculations show unexpected decimal digits?

Because computers represent many decimal values approximately in binary.

---

## 4. Summary — Mistakes & Corrections

### Mistake: Using variables before defining them

This caused:

```text
NameError
```

Correction:

Define the variable first.

### Mistake: Syntax errors

Correction:

Check punctuation, quotes and Python syntax carefully.

### Mistake: Indentation errors

Correction:

Code inside conditional blocks must be indented consistently.

### Mistake: Expecting dependent values to update automatically in REPL

Changing one variable does not automatically recalculate another variable.

The calculation must be executed again.

### Important Lesson

The basic program flow I learned was:

```text
Input
↓
Calculation
↓
Decision
↓
Output
```