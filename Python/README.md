# Python Learning & Portfolio Journey

This repository documents my hands-on Python learning journey and portfolio development.

## Day 1 - Python Fundamentals & Debugging

### What I Practiced
- Variables and data types
- User input with `input()`
- Type conversion using `int()` and `float()`
- Basic calculations
- `if / else` conditions
- f-string formatting
- `round()`

### Mini Exercise
Built a simple sales calculator that:
- Accepts product name, price, and quantity
- Calculates subtotal
- Applies a discount based on order value
- Calculates tax
- Displays the final total

### Debugging Experience
I encountered and fixed:
- `NameError` - incorrect or undefined variable names
- `SyntaxError` - incorrect Python syntax
- `IndentationError` - incorrect indentation
Syntax: print("Text:", variable)
Example: print("Total:", total)
Syntax: print(f"Text: {variable:.2f}")
Example: print(f"Total: {total:.2f}")
Syntax: print("Text:", round(variable, 2))
Example: print("Total:", round(total, 2))

### Code Review Lessons
- Use clear and consistent variable names
- Avoid repeating calculations
- Reuse variables such as `tax_rate`
- Keep business logic easy to read

### Status
Day 1 completed
## Day 2 - Lists and Loops

### Code Review

- `sales = [...]` → **List**
- `sales[3]` → **Index access**
- `for sale in sales:` → **For loop / iteration**
- `if sale > 1000:` → **Conditional statement**
- `sum(sales)` → **Built-in function call**
- `sales.append(7000)` → **Method call**
- `print(sum(sales))` → **Nested function call**
- `print(sales.pop(2))` → **Nested method call**
- `"Total sales:"` → **String literal**
- `total_sales = sum(sales)` → **Assignment statement**
- `sales` in `sum(sales)` → **Argument**

### What I Practiced

- Total, average, highest and lowest sales
- Counting values with `for` + `if`
- Adding, removing and updating list items
- Using indexes
- Formatting numeric output

**Day 2 completed 

# Python Learning & Portfolio Journey

## Day 3 — Dictionaries & Warehouse Inventory Analysis

### What I Did

- Learned Python dictionaries and key-value pairs
- Accessed and updated dictionary values
- Added new key-value pairs
- Used the `.items()` dictionary method
- Learned key-value unpacking
- Created a list of dictionaries
- Looped through multiple product records
- Calculated inventory value using `price × quantity`
- Calculated total warehouse inventory value
- Used initialization and an accumulator
- Used `for` + `if` to detect low-stock products
- Used a counter to count low-stock products
- Practiced debugging indentation errors

---

### Why This Matters

A dictionary can represent one structured business record.

```python
product = {
    "product_name": "Laptop",
    "price": 2000,
    "quantity": 10
}
```

A list of dictionaries can represent multiple business records.

```python
products = [
    {"product_name": "Laptop", "price": 2000, "quantity": 10},
    {"product_name": "Mouse", "price": 20, "quantity": 10}
]
```

This connects later to:

- CSV
- JSON
- SQL tables
- APIs
- Data analysis
- Business reporting

---

### Main Syntax

#### Dictionary

```python
product = {
    "product_name": "Laptop",
    "price": 2000,
    "quantity": 10
}
```

#### Dictionary Key Lookup

```python
product["price"]
```

#### Update a Value

```python
product["price"] = 2200
```

#### Add a New Key-Value Pair

```python
product["category"] = "Computer"
```

#### Dictionary `.items()`

```python
for key, value in product.items():
    print(key, value)
```

#### Loop Through a List of Dictionaries

```python
for item in products:
    print(item["product_name"])
```

#### Inventory Value

```python
result = item["price"] * item["quantity"]
```

#### Accumulator

```python
total_inventory_value = 0

for item in products:
    result = item["price"] * item["quantity"]
    total_inventory_value = total_inventory_value + result
```

#### Condition Inside a Loop

```python
for item in products:
    if item["quantity"] <= 5:
        print(item["product_name"], "is low in stock")
```

#### Counter

```python
low_stock = 0

for item in products:
    if item["quantity"] <= 5:
        low_stock = low_stock + 1
```

---

## Day 3 Mini Project — Warehouse Inventory Analysis

```python
products = [
    {"product_name": "Laptop", "price": 2000, "quantity": 10},
    {"product_name": "Mouse", "price": 20, "quantity": 10},
    {"product_name": "Keyboard", "price": 200, "quantity": 2},
    {"product_name": "Ram", "price": 250, "quantity": 5},
    {"product_name": "SSD", "price": 400, "quantity": 10},
    {"product_name": "Monitor", "price": 300, "quantity": 90}
]

total_inventory_value = 0

for item in products:
    result = item["price"] * item["quantity"]
    total_inventory_value = total_inventory_value + result
    print(item["product_name"], result)

print("Total inventory value in the warehouse is:", total_inventory_value)

for item in products:
    if item["quantity"] <= 5:
        print(item["product_name"], "is low in stock")

low_stock = 0

for item in products:
    if item["quantity"] <= 5:
        low_stock = low_stock + 1

print("Number of low-stock products is:", low_stock)
```

### Output

```text
Laptop 20000
Mouse 200
Keyboard 400
Ram 1250
SSD 4000
Monitor 27000
Total inventory value in the warehouse is: 52850
Keyboard is low in stock
Ram is low in stock
Number of low-stock products is: 2
```

---

## Key Programming Terms

- **Dictionary** — stores data as key-value pairs
- **Key** — identifies a value in a dictionary
- **Value** — data associated with a key
- **Key-value pair** — a key and its associated value
- **Dictionary key lookup** — accessing a value using a key
- **Dictionary method** — a method that belongs to a dictionary
- **`.items()`** — provides dictionary key-value pairs
- **Unpacking** — assigning parts of a pair to separate variables
- **List of dictionaries** — multiple dictionary records stored in a list
- **Record** — one structured set of related data
- **Loop variable** — temporary variable representing the current item
- **Iteration** — one pass through a loop
- **Conditional statement** — decision-making using `if`
- **Comparison expression** — compares two values
- **Initialization** — giving a variable its starting value
- **Accumulator** — stores a running total
- **Accumulation** — repeatedly adding values to an accumulator
- **Counter** — tracks how many times something occurs
- **Indentation** — defines Python code blocks

---

## Code Review

```python
products = [...]
```

→ **List of dictionaries**

```python
{"product_name": "Laptop", "price": 2000, "quantity": 10}
```

→ **Dictionary / Record**

```python
item["price"]
```

→ **Dictionary key lookup**

```python
for item in products:
```

→ **For loop / Iteration**

```python
result = item["price"] * item["quantity"]
```

→ **Assignment statement + Arithmetic expression**

```python
total_inventory_value = 0
```

→ **Initialization**

```python
total_inventory_value = total_inventory_value + result
```

→ **Accumulation**

```python
if item["quantity"] <= 5:
```

→ **Conditional statement + Comparison expression**

```python
low_stock = low_stock + 1
```

→ **Counter increment / Accumulation**

```python
for key, value in product.items():
```

→ **Dictionary iteration + Unpacking**

---

## Interview Quick Q&A — My Day 3 Questions

**Q: Why do we use a `for` loop?**  
A: A `for` loop repeats the same operation for every item in a collection.

**Q: What is the difference between `for` and `if`?**  
A: `for` performs iteration. `if` makes a decision based on a condition.

**Q: Why do we use `for` and `if` together?**  
A: `for` goes through every item, while `if` checks which items meet a condition.

**Q: Why initialize `total_inventory_value = 0`?**  
A: The accumulator needs a starting value before its previous value can be reused.

**Q: Why don't we initialize `result = 0` first?**  
A: `result` receives a new calculated value directly and does not depend on its previous value.

**Q: Why should accumulator initialization be outside the loop?**  
A: If it is inside the loop, the value resets during every iteration.

**Q: What is an accumulator?**  
A: An accumulator is a variable that stores a running total.

**Q: What is a counter?**  
A: A counter tracks how many times something happens.

**Q: What does `.items()` do?**  
A: `.items()` provides the key-value pairs of a dictionary for iteration.

**Q: Why do we write `key, value` with `.items()`?**  
A: Each dictionary item contains a key and a value, and Python unpacks them into two variables.

**Q: Can `.items()` be used directly on `products`?**  
A: No, because `products` is a list. First loop through the list, then use `.items()` on each dictionary.

**Q: What is a list of dictionaries?**  
A: It is a list containing multiple structured dictionary records.

**Q: What is inventory value?**  
A: Inventory value is the monetary value of stock, calculated here as `price × quantity`.

**Q: Why can we calculate directly without storing the result in a variable?**  
A: A calculation can be used directly, but storing it in a variable improves readability and allows reuse.

**Q: What is the difference between `< 5` and `<= 5`?**  
A: `< 5` excludes 5, while `<= 5` includes 5.

**Q: Why is indentation important in Python?**  
A: Indentation tells Python which statements belong inside loops, conditions, and other code blocks.

---

## Day 3 Result

Built a small warehouse inventory analysis program that can:

- Store multiple product records
- Calculate each product's inventory value
- Calculate total warehouse inventory value
- Identify low-stock products
- Count low-stock products

### Connection to Future Learning

```text
Python dictionaries
        ↓
List of business records
        ↓
CSV / JSON
        ↓
SQL tables
        ↓
Data cleaning and analysis
        ↓
Business reports and dashboards
```
## Day 4 — Python Functions

### What I Learned

- What a function is
- How to define a function using `def`
- How to call a function
- Parameters and arguments
- Functions with multiple parameters
- Built-in functions vs user-defined functions
- `print()` vs `return`
- Return values
- Local variables and scope
- Using functions with dictionaries
- Using functions together with `for` loops

---

### Why Functions?

Functions help organize reusable and meaningful logic.

Instead of repeating:

```python
inventory_value = price * quantity
```

the calculation can be given a clear name:

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    return result
```

This makes code easier to reuse, change, test, and understand.

---

### Main Syntax

#### Function Definition

```python
def function_name():
    statement
```

#### Function Call

```python
function_name()
```

#### Function with Parameters

```python
def function_name(parameter):
    statement
```

#### Function with Multiple Parameters

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    return result
```

#### Calling the Function

```python
calculate_inventory(2000, 10)
```

Here:

- `price`, `quantity` → Parameters
- `2000`, `10` → Arguments

---

### `print()` vs `return`

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    print(result)
```

`print()` displays the value.

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    return result
```

`return` sends the value back to the caller so it can be reused.

Example:

```python
inventory_value = calculate_inventory(2000, 10)
print(inventory_value)
```

---

### Function + List of Dictionaries

For one specific dictionary:

```python
inventory_value = calculate_inventory(
    products[0]["price"],
    products[0]["quantity"]
)

print(inventory_value)
```

For every dictionary:

```python
for item in products:
    inventory_value = calculate_inventory(
        item["price"],
        item["quantity"]
    )

    print(item["product_name"], inventory_value)
```

Connection:

```text
for loop
→ handles repetition

function
→ handles reusable calculation logic
```

---

### Scope

A variable created inside a function is normally a local variable.

```python
def calculate_inventory(price, quantity):
    result = price * quantity
    return result
```

Here:

```python
result
```

is a local variable.

Trying to access it directly outside the function can cause:

```text
NameError: name 'result' is not defined
```

`return` sends the value outside the function. It does not move the local variable itself outside.

---

## Key Programming Terms

- Function
- Function definition
- Function call
- Built-in function
- User-defined function
- Parameter
- Argument
- Statement
- Expression
- Return statement
- Return value
- Local variable
- Local scope
- Scope
- Nested function call

---

## Code Review

```python
def calculate_inventory(price, quantity):
```

→ Function definition with two parameters

```python
price
quantity
```

→ Parameters

```python
result = price * quantity
```

→ Assignment statement with arithmetic expression

```python
return result
```

→ Return statement

```python
calculate_inventory(2000, 10)
```

→ Function call

```python
2000, 10
```

→ Arguments

```python
inventory_value = calculate_inventory(2000, 10)
```

→ Assignment receiving a return value

```python
print(calculate_inventory(500, 3))
```

→ Nested function call

```python
for item in products:
```

→ Iteration

```python
calculate_inventory(
    item["price"],
    item["quantity"]
)
```

→ Function call using dictionary values as arguments

---

## Interview Quick Q&A — My Day 4 Questions

**Q: What is a function?**  
A: A function is a reusable block of code designed to perform a specific task.

**Q: What is a parameter?**  
A: A parameter is a variable in a function definition that receives input.

**Q: What is an argument?**  
A: An argument is the actual value passed to a function when it is called.

**Q: What is a statement?**  
A: A statement is an instruction that tells Python to perform an action.

**Q: What is the difference between a parameter and an argument?**  
A: A parameter is defined in the function; an argument is the actual value supplied when calling it.

**Q: Is `print()` a function?**  
A: Yes. `print()` is a built-in Python function.

**Q: What is a user-defined function?**  
A: A function created by the programmer using `def`.

**Q: Why should I not create my own function named `print`?**  
A: It would shadow Python's built-in `print()` function.

**Q: Why use `return` instead of only `print()`?**  
A: `print()` displays a value, while `return` sends a value back so it can be reused elsewhere.

**Q: Can I write `print(calculate_inventory(500, 3))`?**  
A: Yes. The inner function returns a value, and `print()` displays that returned value.

**Q: When should I use a function and when should I use a `for` loop?**  
A: Use a `for` loop for repetition. Use a function to organize and reuse specific logic. They can also be used together.

**Q: Why do `price` and `quantity` appear both in the function and in the loop?**  
A: Inside the function they are parameters. In the function call, dictionary values are passed as arguments to those parameters.

**Q: What is scope?**  
A: Scope determines where a variable can be accessed in a program.

**Q: What is a local variable?**  
A: A local variable is created inside a function and is normally accessible only inside that function.

**Q: Does `return` make a local variable available outside the function?**  
A: No. It returns the variable's value, not the local variable itself.

**Q: Why is scope useful?**  
A: Scope prevents variable conflicts and helps keep functions independent and easier to debug.

---

## Day 4 Result

I can now:

- Define and call functions
- Pass values using parameters and arguments
- Return calculated values
- Understand the difference between `print()` and `return`
- Understand local variables and scope
- Use dictionary values as function arguments
- Combine functions with `for` loops
- Separate reusable business logic from repetition

### Connection to Future Learning

```text
Functions
    ↓
Reusable business logic
    ↓
Data cleaning functions
    ↓
File processing
    ↓
CSV processing
    ↓
Larger Python programs
    ↓
Testing and automation
```
