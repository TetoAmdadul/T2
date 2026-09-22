# Python Learning Diary

This repository documents my Python learning journey from fundamentals to practical data analysis projects.

My main goal is to build a strong foundation in Python and gradually connect it with SQL, data analysis, Power BI, and Data Engineering.

---

# Day 1 — Python Fundamentals

## 1. What Did I Learn Today?

- Learned what a variable is.
- Learned basic Python data types.
- Learned how to take user input using `input()`.
- Learned type conversion using:
  - `int()`
  - `float()`
  - `str()`
- Learned conditional statements:
  - `if`
  - `elif`
  - `else`
- Learned the difference between an expression and a statement.
- Learned how f-strings work.
- Learned how `round()` works.
- Learned the difference between rounding a numeric value and formatting a number for display.

### Variable

A variable is a name that refers to or stores a value.

Example:

```python
price = 100
quantity = 3
```

### Expression

An expression is code that produces a value.

Example:

```python
price * quantity
```

### Statement

A statement is a complete instruction for Python.

Example:

```python
total = price * quantity
```

The statement contains the expression:

```python
price * quantity
```

### f-string

Standard syntax:

```python
f"Text {expression}"
```

Example:

```python
name = "Amina"
print(f"Customer name is {name}")
```

The `{}` part is called a placeholder or replacement field.

### Formatting decimal places

Example:

```python
average = 10.5678

print(f"Average: {average:.2f}")
```

Output:

```text
Average: 10.57
```

### `round()`

Example:

```python
average = 10.5678

rounded_average = round(average, 2)
print(rounded_average)
```

`round()` returns a rounded numeric value.

`:.2f` is mainly used for display formatting.

---

## 2. What Did I Do Today?

- Created variables.
- Performed basic calculations.
- Used `input()` to receive values.
- Converted input values into numbers.
- Used `if`, `elif`, and `else`.
- Practiced arithmetic expressions.
- Printed results using normal `print()`.
- Printed formatted results using f-strings.
- Practiced `round()` and decimal formatting.

Example:

```python
price = 100
quantity = 3

total = price * quantity

print(f"Total price is {total}")
```

---

## 3. Interview Questions & Answers

**Q: What is a variable in Python?**

A: A variable is a name that refers to a value stored in memory.

**Q: What is an expression?**

A: An expression is code that produces a value.

Example:

```python
price * quantity
```

**Q: What is a statement?**

A: A statement is a complete instruction for Python to perform an action.

Example:

```python
total = price * quantity
```

**Q: What is the difference between an expression and a statement?**

A: An expression produces a value, while a statement is an instruction for Python to perform an action.

**Q: What is an f-string?**

A: An f-string is a formatted string that allows expressions or variables to be inserted directly inside a string using curly braces.

**Q: What is the difference between `round()` and `:.2f`?**

A: `round()` returns a rounded numeric value, while `:.2f` formats a value for display with exactly two decimal places.

---

## 4. Summary — Mistakes & Corrections

- I learned that values returned by `input()` are strings by default.
  - Correction: Convert them using `int()` or `float()` when numeric operations are needed.

- I initially needed more clarity about expressions and statements.
  - Correction: An expression produces a value, while a statement performs an instruction.

- I learned that `round()` and `:.2f` are related but not identical.
  - `round()` changes the numeric result.
  - `:.2f` controls how the result is displayed.

---

# Day 2 — Lists and Loops

## 1. What Did I Learn Today?

- Learned what a list is.
- Learned that lists are ordered collections.
- Learned that Python list indexes start from `0`.
- Learned how to access list elements using an index.
- Learned how `for` loops work.
- Learned the meaning of iteration.
- Learned the naming convention:
  - collection name → plural
  - loop variable → singular
- Learned built-in functions:
  - `sum()`
  - `len()`
  - `max()`
  - `min()`
- Learned how counters work.
- Learned common list methods:
  - `.append()`
  - `.remove()`
  - `.insert()`
  - `.pop()`

### List

A list stores multiple values.

Example:

```python
sales = [1200, 1500, 2200, 900]
```

### List index

```python
print(sales[0])
```

Output:

```text
1200
```

Python indexing starts from `0`.

### Loop

```python
for sale in sales:
    print(sale)
```

Literal meaning:

> For each sale inside sales, execute the following code.

### Naming convention

```python
customers = ["Amina", "Rafi", "Sara"]

for customer in customers:
    print(customer)
```

`customers` represents the collection.

`customer` represents one item during each iteration.

### Counter

```python
count = 0

for sale in sales:
    if sale > 1000:
        count = count + 1
```

A counter normally starts at `0` because nothing has been counted yet.

---

## 2. What Did I Do Today?

- Created Python lists.
- Accessed values using indexes.
- Practiced looping through lists.
- Calculated totals using `sum()`.
- Counted items using `len()`.
- Found highest values using `max()`.
- Found lowest values using `min()`.
- Practiced counters with conditions.
- Added items using `.append()`.
- Removed items from lists.
- Practiced changing list contents.

Example:

```python
sales = [1200, 1500, 2200, 900]

total = sum(sales)
number_of_sales = len(sales)
highest = max(sales)
lowest = min(sales)

print(total)
print(number_of_sales)
print(highest)
print(lowest)
```

---

## 3. Interview Questions & Answers

**Q: What is a list in Python?**

A: A list is an ordered collection that can store multiple values.

**Q: What is an index?**

A: An index represents the position of an item inside a collection such as a list.

**Q: What index does a Python list start from?**

A: Python list indexes start from `0`.

**Q: What is a loop?**

A: A loop repeats a block of code.

**Q: What is iteration?**

A: Iteration is one cycle or repetition of a loop.

**Q: What is a counter?**

A: A counter is a variable used to count how many times something occurs.

---

## 4. Summary — Mistakes & Corrections

- I needed to remember that Python list indexes start at `0`.

- I learned why counters usually start at `0`.
  - Before processing anything, zero items have been counted.

- I learned a useful naming convention:

```python
for customer in customers:
```

instead of using unclear names.

- I learned that list built-in functions can often simplify calculations.

---

# Day 3 — Dictionaries and Structured Data

## 1. What Did I Learn Today?

- Learned what a dictionary is.
- Learned key-value pairs.
- Learned that one dictionary can represent one record.
- Learned that a list of dictionaries can represent multiple records.
- Learned how to access dictionary values using keys.
- Learned how dictionaries and lists can be nested.
- Learned the difference between:
  - list access
  - dictionary access
  - object access
  - function calls
- Learned the difference between a counter and an accumulator.

### Dictionary

A dictionary stores data using key-value pairs.

Example:

```python
customer = {
    "name": "Amina",
    "city": "Helsinki",
    "sales": 3200
}
```

Access:

```python
print(customer["name"])
```

### One dictionary = one record

```python
customer = {
    "name": "Amina",
    "city": "Helsinki",
    "sales": 3200
}
```

This can represent one customer record.

### List of dictionaries = multiple records

```python
customers = [
    {
        "name": "Amina",
        "sales": 3200
    },
    {
        "name": "Rafi",
        "sales": 1400
    }
]
```

### Access patterns

List:

```python
sales[0]
```

Dictionary:

```python
customer["name"]
```

Object:

```python
customer.name
```

Function:

```python
calculate_total(customer)
```

### Dictionary inside a list

```python
print(customers[0]["name"])
```

First:

```python
customers[0]
```

selects the first dictionary.

Then:

```python
["name"]
```

selects the value associated with the `"name"` key.

### List inside a dictionary

```python
customer = {
    "name": "Amina",
    "orders": [100, 200, 300]
}
```

Access:

```python
customer["orders"][0]
```

---

## 2. What Did I Do Today?

- Created dictionaries.
- Accessed dictionary values using keys.
- Modified existing dictionary values.
- Added new keys to dictionaries.
- Created lists of dictionaries.
- Practiced looping through multiple records.
- Practiced nested data structures.

Example:

```python
customers = [
    {"name": "Amina", "sales": 3200},
    {"name": "Rafi", "sales": 1400}
]

for customer in customers:
    print(customer["name"], customer["sales"])
```

Modified a value:

```python
customers[1]["sales"] = 2000
```

Added a new key:

```python
customers[1]["country"] = "Finland"
```

---

## 3. Interview Questions & Answers

**Q: What is a dictionary in Python?**

A: A dictionary is a collection that stores data as key-value pairs.

**Q: What is the difference between a list and a dictionary?**

A: A list normally accesses items by numerical index, while a dictionary accesses values using keys.

**Q: What can one dictionary represent in data analysis?**

A: One dictionary can represent one record or row.

**Q: What can a list of dictionaries represent?**

A: A list of dictionaries can represent multiple structured records.

**Q: What is the difference between a counter and an accumulator?**

A: A counter counts occurrences, while an accumulator collects or adds values over time.

---

## 4. Summary — Mistakes & Corrections

- I initially tried to think about dictionary access like list indexing.

Incorrect idea:

```python
customers[1][2]
```

when the dictionary uses string keys.

Correct:

```python
customers[1]["sales"]
```

- I learned to identify the structure first:
  - list → use index
  - dictionary → use key
  - object → use attribute
  - function → call using parentheses

- I learned the important data connection:

```text
List = many items
Dictionary = one structured record
List of dictionaries = many structured records
```

This later connects naturally with CSV, JSON, pandas, and SQL tables.

---

# Day 4 — Functions, Parameters, Return and Scope

## 1. What Did I Learn Today?

- Learned what a function is.
- Learned how to define functions using `def`.
- Learned parameters.
- Learned arguments.
- Learned `return`.
- Learned local variables.
- Learned variable scope.
- Learned why functions help organize reusable logic.

### Function

A function is a reusable block of code designed to perform a specific task.

Example:

```python
def calculate_total(customer):
    total = sum(customer["orders"])
    return total
```

### Parameter

In:

```python
def calculate_total(customer):
```

`customer` is a parameter.

A parameter is a placeholder that receives data when the function is called.

### Argument

In:

```python
calculate_total(customers[0])
```

`customers[0]` is the argument.

An argument is the actual value supplied to the function.

### Return

```python
return total
```

`return` sends a value from the function back to the place where the function was called.

### Scope

Scope defines the region where a variable can be accessed.

Example:

```python
def calculate_total(customer):
    total = sum(customer["orders"])
    return total
```

`total` is a local variable.

Normally it can only be accessed inside the function.

But its value can be sent outside using:

```python
return total
```

---

## 2. What Did I Do Today?

- Created functions.
- Passed dictionaries into functions.
- Used parameters.
- Used arguments.
- Returned calculated values.
- Called functions inside loops.
- Practiced separating reusable logic from repeated loops.

Example:

```python
def calculate_total(customer):
    total = sum(customer["orders"])
    return total


for customer in customers:
    total = calculate_total(customer)
    print(customer["name"], total)
```

---

## 3. Interview Questions & Answers

**Q: What is a function?**

A: A function is a reusable block of code that performs a specific task.

**Q: What is a parameter?**

A: A parameter is a variable defined in a function definition that receives data when the function is called.

**Q: What is an argument?**

A: An argument is the actual value passed to a function.

**Q: What is the difference between a parameter and an argument?**

A: A parameter is the placeholder in the function definition, while an argument is the actual value supplied during the function call.

**Q: What does `return` do?**

A: `return` sends a value from a function back to the place where the function was called.

**Q: What is scope?**

A: Scope defines the region where a variable can be accessed.

**Q: What is a local variable?**

A: A local variable is a variable created inside a function and normally accessible only inside that function.

---

## 4. Summary — Mistakes & Corrections

- I initially found parameter selection difficult.

A useful question is:

> What information does this function need to do its job?

That information usually becomes the parameter.

- I learned that functions should normally be defined once and then called when needed.

Instead of defining a function repeatedly inside a loop:

```python
def calculate_total(customer):
    return sum(customer["orders"])

for customer in customers:
    total = calculate_total(customer)
```

- I learned that `return` sends the value, not the local variable itself.

---

# Day 5 — Nested Data and Nested Loops

## 1. What Did I Learn Today?

- Learned nested data structures.
- Learned nested loops.
- Learned the difference between separate loops and nested loops.
- Learned when an inner loop is necessary.
- Learned when built-in functions can replace explicit loops.
- Learned that functions and loops solve different problems.

### Nested loop

A nested loop is a loop inside another loop.

Example:

```python
for customer in customers:
    for order in customer["orders"]:
        print(customer["name"], order)
```

The outer loop processes customers.

The inner loop processes each customer's individual orders.

### Main decision rule

If I need every individual item from an inner collection, I may need an inner loop.

Example:

```python
for customer in customers:
    for order in customer["orders"]:
        print(order)
```

But if I only need a total:

```python
for customer in customers:
    total = sum(customer["orders"])
```

I do not need to write an explicit inner loop.

### Separate loops

These are two separate loops:

```python
for customer in customers:
    print(customer["name"])

for customer in customers:
    print(customer["city"])
```

The first loop finishes completely before the second loop starts.

### Nested loops

```python
for customer in customers:
    for order in customer["orders"]:
        print(order)
```

The inner loop runs while the outer loop is processing each customer.

---

## 2. What Did I Do Today?

- Practiced dictionaries containing lists.
- Practiced lists containing dictionaries.
- Practiced nested loops.
- Calculated totals from inner lists.
- Compared explicit loops with built-in functions.
- Practiced deciding whether an inner loop was necessary.

Example:

```python
customers = [
    {
        "name": "Amina",
        "orders": [100, 200, 300]
    },
    {
        "name": "Rafi",
        "orders": [400, 500]
    }
]

for customer in customers:
    total = sum(customer["orders"])
    print(customer["name"], total)
```

---

## 3. Interview Questions & Answers

**Q: What is a nested loop?**

A: A nested loop is a loop inside another loop.

**Q: When do we need a nested loop?**

A: A nested loop is useful when we need to process individual items inside another collection.

**Q: Do we always need an inner loop for a list inside a dictionary?**

A: No. If we only need an aggregate such as `sum()`, `max()`, `min()`, or `len()`, a built-in function may remove the need for an explicit inner loop.

**Q: What is the difference between separate loops and nested loops?**

A: Separate loops run one after another. In nested loops, one loop runs inside another loop.

---

## 4. Summary — Mistakes & Corrections

- I initially thought nested data automatically required nested loops.
  - Correction: The required operation determines whether an inner loop is necessary.

- I learned this rule:

> If I need each individual item, use an inner loop.

- I learned that built-in functions such as:

```python
sum()
max()
min()
len()
```

can sometimes replace an explicit loop.

- I learned that a function does not automatically replace a nested loop.
  - Functions organize reusable logic.
  - Loops control repetition.

---

# Day 6 — File Handling

## 1. What Did I Learn Today?

- Learned how to open files in Python.
- Learned the `with open()` pattern.
- Learned file modes:
  - `"r"` — read
  - `"w"` — write
  - `"a"` — append
- Learned `.read()`.
- Learned `.write()`.
- Learned `.strip()`.
- Learned newline character `\n`.
- Learned why `with open()` is useful.
- Learned the difference between:
  - object methods
  - module functions

### Opening a file

```python
with open("filename.txt", "r") as file:
    content = file.read()
```

### Literal meaning

```python
with open("filename.txt", "r") as file:
```

means:

> Open the file in read mode and temporarily refer to the opened file object using the name `file`.

### Reading

```python
content = file.read()
```

`file.read()` reads the opened file contents as raw text.

### Writing

```python
with open("report.txt", "w") as file:
    file.write("Sales report")
```

### Append

```python
with open("report.txt", "a") as file:
    file.write("\nNew report line")
```

### `.strip()`

```python
text = "  Python  "
clean_text = text.strip()
```

`.strip()` removes leading and trailing whitespace.

---

## 2. What Did I Do Today?

- Created text files.
- Opened files in read mode.
- Read file contents.
- Wrote data into files.
- Appended new data.
- Practiced handling newline characters.
- Practiced cleaning text using `.strip()`.
- Connected file handling with future CSV processing.

Example:

```python
with open("customer_report.txt", "r") as file:
    content = file.read()

print(content)
```

---

## 3. Interview Questions & Answers

**Q: What does `open()` do?**

A: `open()` opens a file and returns a file object.

**Q: Why use `with open()`?**

A: `with open()` manages the file safely and automatically closes it when the block finishes.

**Q: What does `"r"` mean?**

A: `"r"` means read mode.

**Q: What does `"w"` mean?**

A: `"w"` means write mode. It writes to the file and can replace existing contents.

**Q: What does `"a"` mean?**

A: `"a"` means append mode. It adds new content to the end of the file.

**Q: What does `file.read()` do?**

A: It reads the contents of an opened file as raw text.

---

## 4. Summary — Mistakes & Corrections

- I needed to distinguish between opening a file and interpreting its data.

`open()` gives access to the file.

```python
file.read()
```

reads raw text.

Later, CSV tools can interpret that file as structured CSV data.

- I learned the syntax difference:

Object method:

```python
object.method()
```

Example:

```python
file.read()
```

Module function:

```python
module.function(argument)
```

Example:

```python
csv.reader(file)
```

---

# Day 7 — CSV Files and Structured Data

## 1. What Did I Learn Today?

- Learned what CSV means.
- Learned CSV structure:
  - header
  - row / record
  - column
- Learned `import csv`.
- Learned `csv.reader()`.
- Learned `csv.DictReader()`.
- Learned how to skip headers using `next()`.
- Learned that CSV values are initially strings.
- Learned type conversion for CSV values.
- Learned basic CSV writing.
- Connected CSV data with lists and dictionaries.
- Learned the difference between raw file reading and CSV parsing.

### CSV

CSV means:

> Comma-Separated Values

Example:

```csv
name,city,sales
Amina,Helsinki,3200
Rafi,Espoo,1400
Bob,Vantaa,4300
```

### Importing CSV module

```python
import csv
```

This imports Python's built-in CSV module.

It does not import a CSV file.

### `csv.reader()`

```python
import csv

with open("sales.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

`csv.reader()` normally represents each row as a list.

### `csv.DictReader()`

```python
import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
        print(row["sales"])
```

`csv.DictReader()` uses the CSV header as dictionary keys.

Example row:

```python
{
    "name": "Amina",
    "city": "Helsinki",
    "sales": "3200"
}
```

### CSV values are strings

Even though the CSV contains:

```text
3200
```

Python initially reads it as:

```python
"3200"
```

Therefore:

```python
sale = int(row["sales"])
```

converts it into an integer.

### CSV writer

```python
with open("report.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "sales"])
```

---

## 2. What Did I Do Today?

- Opened CSV files.
- Used `csv.reader()`.
- Used `next(reader)` to skip headers.
- Used `csv.DictReader()`.
- Accessed CSV columns using keys.
- Converted numeric strings to integers.
- Used loops to process CSV rows.
- Stored values from CSV files inside Python lists.
- Practiced writing CSV rows.
- Connected CSV data with previous list and dictionary knowledge.

Example:

```python
import csv

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sale = int(row["sales"])

        print(row["name"], sale)
```

---

## 3. Interview Questions & Answers

**Q: What does CSV stand for?**

A: CSV stands for Comma-Separated Values.

**Q: What is a CSV file?**

A: A CSV file is a text-based format commonly used to store tabular data.

**Q: What does `import csv` do?**

A: It imports Python's built-in CSV module.

**Q: What is the difference between `file.read()` and `csv.reader(file)`?**

A: `file.read()` reads raw text, while `csv.reader(file)` interprets the file as CSV rows.

**Q: What is the difference between `csv.reader()` and `csv.DictReader()`?**

A: `csv.reader()` normally returns rows as lists, while `csv.DictReader()` returns rows as dictionaries using header names as keys.

**Q: Why do we use `int(row["sales"])`?**

A: CSV values are read as strings, so `int()` converts a numeric string into an integer.

---

## 4. Summary — Mistakes & Corrections

- I initially thought there might be:

```python
csv.read()
```

Correction:

Raw file reading:

```python
file.read()
```

CSV parsing:

```python
csv.reader(file)
```

or:

```python
csv.DictReader(file)
```

- I needed to understand why:

```python
print(row["sales"])
```

prints many sales values.

Correction:

`row["sales"]` returns one sales value for the current row, but the `for` loop repeats once for every row.

- I learned this connection:

```text
CSV row
    ↓
DictReader
    ↓
Python dictionary
```

---

# Extra Practice — Classes, Objects and OOP Basics

## 1. What Did I Learn Today?

- Learned the basic concept of Object-Oriented Programming.
- Learned what a class is.
- Learned what an object is.
- Learned what an instance is.
- Learned what `__init__` does.
- Learned what `self` means.
- Learned what attributes are.
- Learned what methods are.
- Learned class naming conventions.
- Connected classes with `csv.DictReader`.

### Class

A class is a blueprint for creating objects.

Example:

```python
class Customer:
    pass
```

Class names normally use PascalCase:

```python
Customer
SalesReport
BankAccount
```

### Object / Instance

An object is an actual item created from a class.

Example:

```python
customer1 = Customer()
```

`customer1` is an object or instance of `Customer`.

### `__init__`

Example:

```python
class Customer:

    def __init__(self, name):
        self.name = name
```

`__init__` is a special initialization method that runs when an object is created.

### `self`

`self` represents the current object.

Example:

```python
self.name = name
```

This stores the supplied `name` value as an attribute of the current object.

### Attribute

```python
customer1.name
```

`name` is an attribute.

An attribute stores data related to an object.

### Method

A method is a function defined inside a class.

Example:

```python
class Customer:

    def greet(self):
        print("Hello")
```

`greet()` is a method.

### Connection with `csv.DictReader`

```python
reader = csv.DictReader(file)
```

`DictReader` is a class from Python's `csv` module.

The expression:

```python
csv.DictReader(file)
```

creates a `DictReader` object or instance.

Then:

```python
reader
```

stores a reference to that object.

---

## 2. What Did I Do Today?

- Created simple classes.
- Created objects from classes.
- Practiced `__init__`.
- Practiced `self`.
- Created object attributes.
- Practiced methods.
- Connected OOP concepts with previously used Python tools such as `csv.DictReader`.

Example:

```python
class Customer:

    def __init__(self, name, city):
        self.name = name
        self.city = city


customer1 = Customer("Amina", "Helsinki")

print(customer1.name)
print(customer1.city)
```

---

## 3. Interview Questions & Answers

**Q: What is a class?**

A: A class is a blueprint used to create objects.

**Q: What is an object?**

A: An object is an instance created from a class.

**Q: What is an instance?**

A: An instance is a specific object created from a class.

**Q: What is `__init__`?**

A: `__init__` is a special initialization method that runs when an object is created.

**Q: What does `self` represent?**

A: `self` represents the current object or instance.

**Q: What is an attribute?**

A: An attribute is data associated with an object.

**Q: What is a method?**

A: A method is a function defined inside a class.

---

## 4. Summary — Mistakes & Corrections

- I initially needed clarity about the difference between class and object.

Correction:

```text
Class = blueprint
Object = actual instance created from the blueprint
```

- I learned that:

```python
csv.DictReader
```

is a class.

And:

```python
reader = csv.DictReader(file)
```

creates an instance.

- I learned that object data is normally accessed using dot notation:

```python
customer.name
```

while dictionary values are accessed using keys:

```python
customer["name"]
```

---

# Extra Practice — Variable Initialization and State

## 1. What Did I Learn Today?

- Learned what initialization means.
- Learned the difference between initialization and reassignment.
- Learned why some variables must be created before a loop.
- Learned how variables can preserve state between loop iterations.
- Learned why `lowest_sale = 0` is not always a good initialization strategy.
- Learned how to initialize lowest/highest values using real data.

### Initialization

Initialization means assigning a variable its first starting value.

Example:

```python
total_sales = 0
```

### Update / Reassignment

```python
total_sales = total_sales + sale
```

This updates an existing value.

### Counter initialization

```python
count = 0
```

The counter starts at zero because no records have been processed yet.

### Current item

A variable representing the current item normally belongs inside the loop.

Example:

```python
for row in reader:
    sale = int(row["sales"])
```

`sale` changes during each iteration.

### Persistent state

Variables that must remember information between loop iterations normally need to exist outside or be initialized before repeated updates.

Example:

```python
total_sales = 0

for row in reader:
    sale = int(row["sales"])
    total_sales = total_sales + sale
```

### Lowest sale problem

This can be unreliable:

```python
lowest_sale = 0
```

if all real sales values are positive.

A better learning pattern is to use the first real value:

```python
count = count + 1

if count == 1:
    lowest_sale = sale

elif sale < lowest_sale:
    lowest_sale = sale
```

---

## 2. What Did I Do Today?

- Practiced counters.
- Practiced accumulators.
- Practiced variable initialization.
- Practiced updating variables inside loops.
- Practiced highest and lowest value logic.
- Connected initialization with CSV record processing.

---

## 3. Interview Questions & Answers

**Q: What is variable initialization?**

A: Initialization means assigning the first starting value to a variable.

**Q: What is reassignment?**

A: Reassignment means assigning a new value to a variable that already exists.

**Q: Why are counters usually initialized before a loop?**

A: Because the counter needs to preserve its value across multiple loop iterations.

**Q: Why can initializing a lowest value to `0` be a problem?**

A: If all real values are positive, none of them may be lower than zero, so the result would be incorrect.

---

## 4. Summary — Mistakes & Corrections

- I initially wondered why some variables were created before loops while others were created inside loops.

Correction:

Current-item values can normally be created inside the loop:

```python
sale = int(row["sales"])
```

Persistent state normally exists before repeated updates:

```python
count = 0
total = 0
```

- I learned that initialization should make logical sense for the data.

---

# Portfolio Project 01 — Sales Data Analysis

## 1. What Did I Learn Today?

- Learned how previously studied Python concepts work together in a real project.
- Connected:
  - file handling
  - CSV
  - dictionaries
  - lists
  - loops
  - conditions
  - functions
  - parameters
  - arguments
  - return values
  - scope
  - counters
  - type conversion
  - built-in functions
- Learned how to calculate business-style metrics from CSV data.
- Learned the difference between manual accumulator logic and using Python built-in functions.
- Learned how a function parameter and argument can use different variable names.
- Learned the difference between a function definition and a decorator.
- Learned basic Git and GitHub workflow for a portfolio project.

### Project data

```csv
name,city,sales
Amina,Helsinki,3200
Rafi,Espoo,1400
Bob,Vantaa,4300
Sara,Tampere,2700
Mika,Turku,5100
```

### Expected analysis

```text
Sales: [3200, 1400, 4300, 2700, 5100]

Total sales: 16700

Average sales: 3340.0

Lowest sale:
Rafi — 1400

Highest sale:
Mika — 5100

Sales above 3000:
3
```

### Custom average function

```python
def average_sales(total_sales, number_of_sellers):
    average = total_sales / number_of_sellers
    return average
```

Function parameters:

```python
total_sales
number_of_sellers
```

When calling:

```python
average_sales(total, sellers)
```

the arguments are:

```python
total
sellers
```

The names do not need to match.

### Reading the CSV

```python
with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
```

### Collecting sales

```python
sales = []

for row in reader:
    sale = int(row["sales"])
    sales.append(sale)
```

### Calculations

```python
total = sum(sales)
sellers = len(sales)
lowest_sale = min(sales)
highest_sale = max(sales)
```

### Counting sales above 3000

```python
count = 0

for sale in sales:
    if sale > 3000:
        count = count + 1
```

### Average

```python
average_sales(total, sellers)
```

---

## 2. What Did I Do Today?

- Built my first complete Python portfolio project.
- Created a CSV dataset.
- Read the CSV using `csv.DictReader`.
- Converted sales strings into integers.
- Stored sales values inside a list.
- Calculated total sales.
- Calculated average sales.
- Found minimum sales.
- Found maximum sales.
- Identified lowest seller.
- Identified highest seller.
- Counted sales greater than 3000.
- Created a reusable average function.
- Printed formatted analysis results.
- Created a dedicated local portfolio project folder.
- Created a Git repository.
- Added files to Git.
- Created the first commit.
- Created a GitHub repository.
- Connected the local repository with GitHub.
- Successfully pushed the portfolio project to GitHub.

Project files:

```text
README.md
portfolio_01_sales_data_analysis.py
sales.csv
```

---

## 3. Interview Questions & Answers

**Q: Why use `csv.DictReader` for this project?**

A: `csv.DictReader` allows CSV columns to be accessed by their header names, which makes the code easier to read and understand.

**Q: Why convert `row["sales"]` to an integer?**

A: CSV values are initially strings, so numeric calculations require conversion.

Example:

```python
sale = int(row["sales"])
```

**Q: Why store sales in a list?**

A: Storing the values in a list makes it easy to use built-in functions such as `sum()`, `len()`, `min()`, and `max()`.

**Q: Why create a function for average sales?**

A: The function organizes the calculation as reusable logic and demonstrates parameters, arguments, return values, and scope.

**Q: Do function parameter names and argument variable names need to match?**

A: No. The parameter receives the value supplied by the argument regardless of whether their variable names are the same.

Example:

```python
def average_sales(total_sales, number_of_sellers):
    return total_sales / number_of_sellers
```

Call:

```python
average_sales(total, sellers)
```

**Q: What is the difference between a function definition and a decorator?**

A: A function definition creates a function using `def`. A decorator is a separate Python feature used to modify or extend the behaviour of functions or classes.

---

## 4. Summary — Mistakes & Corrections

- I initially confused a function definition with a decorator.
  - Correction: `def` defines a function. A decorator is a different concept.

- I initially thought the parameter and argument variable names might need to match.
  - Correction: They can have different names.

Example:

```python
def average_sales(total_sales, number_of_sellers):
    return total_sales / number_of_sellers

average_sales(total, sellers)
```

- I learned that CSV values must be converted before mathematical calculations.

```python
sale = int(row["sales"])
```

- I learned that the project currently assumes sales data exists.
  - Future versions can add validation and error handling.

- I learned that tied minimum or maximum values may require additional logic if multiple sellers have exactly the same sales.

- I learned the value of building projects:
  - isolated Python concepts became easier to understand when connected together.

---

# Git and GitHub — Project Workflow

## 1. What Did I Learn Today?

- Learned the difference between Git and GitHub.
- Learned what a Git repository is.
- Learned `git init`.
- Learned `git status`.
- Learned staging with `git add`.
- Learned commits.
- Learned remote repositories.
- Learned `origin`.
- Learned `git push`.
- Learned branch tracking.
- Learned how to separate learning repositories from portfolio repositories.

### Git initialization

```bash
git init
```

This creates a Git repository inside the current project folder.

### Check status

```bash
git status
```

### Stage files

```bash
git add .
```

### Commit

```bash
git commit -m "Add first sales data analysis portfolio project"
```

### Connect GitHub repository

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY.git
```

### Push

```bash
git push -u origin main
```

The `-u` connects the local `main` branch with the remote `origin/main` branch for future pushes.

After that, future updates normally use:

```bash
git add .
git commit -m "Describe the update"
git push
```

---

## 2. What Did I Do Today?

- Initialized the project repository using:

```bash
git init
```

- Checked files using:

```bash
git status
```

- Staged project files:

```bash
git add .
```

- Created the first commit:

```bash
git commit -m "Add first sales data analysis portfolio project"
```

- Connected the local repository with GitHub.
- Successfully pushed the `main` branch to GitHub.

---

## 3. Interview Questions & Answers

**Q: What is Git?**

A: Git is a distributed version control system used to track changes in files and code.

**Q: What is GitHub?**

A: GitHub is an online platform used to host and collaborate on Git repositories.

**Q: What does `git init` do?**

A: `git init` creates a new Git repository in the current directory.

**Q: What does `git add` do?**

A: `git add` moves file changes into the staging area for the next commit.

**Q: What is a commit?**

A: A commit is a saved snapshot of staged changes in Git history.

**Q: What is `origin`?**

A: `origin` is the conventional name used for the main remote Git repository.

**Q: What does `git push` do?**

A: `git push` sends local commits to a remote repository such as GitHub.

---

## 4. Summary — Mistakes & Corrections

- I learned that `git init` should not be repeated every time I modify the same project.

For an existing repository, the normal workflow is:

```bash
git add .
git commit -m "Describe the update"
git push
```

- I learned that a completely new meaningful project can have its own repository.

- I learned that daily practice and learning notes can remain inside my `T2` repository.

- Finished portfolio projects can have separate repositories.

My current structure is conceptually:

```text
T2
└── Learning, practice, exercises and notes

Portfolio
└── Separate finished projects
```

This keeps learning history and recruiter-facing portfolio projects organized separately.

---

# Current Learning Position

So far, I have studied and practiced:

```text
Python Fundamentals
        ↓
Variables and Data Types
        ↓
Conditions
        ↓
Lists
        ↓
Loops
        ↓
Dictionaries
        ↓
Functions
        ↓
Parameters and Arguments
        ↓
Return and Scope
        ↓
Nested Data
        ↓
Nested Loops
        ↓
File Handling
        ↓
CSV
        ↓
DictReader
        ↓
Classes and Objects
        ↓
Variable Initialization
        ↓
Practical Sales Data Analysis Project
        ↓
Git and GitHub
```

The most important connection I have learned is:

```text
List
= many values

Dictionary
= one structured record

List of Dictionaries
= many structured records

CSV
= tabular data stored in a file

csv.DictReader
= converts CSV rows into dictionary-like records

Functions
= reusable logic

Loops
= repetition

return
= sends a result from a function

Scope
= determines where variables can be accessed
```

These concepts create the foundation for future work with:

```text
Python
SQL
pandas
Data Cleaning
Data Analysis
Power BI
APIs
JSON
Databases
ETL / ELT
Data Engineering
```

---

# Portfolio Progress

## Project 01 — Sales Data Analysis

Completed first version.

Technologies and concepts used:

```text
Python
CSV
csv.DictReader
Lists
Dictionaries
Loops
Conditions
Functions
Parameters
Arguments
Return
Scope
Type Conversion
Counters
sum()
len()
min()
max()
round()
Git
GitHub
```

Future improvements may include:

```text
Data validation
Error handling
Data cleaning
Additional KPIs
pandas
Data visualization
SQL
Power BI
```

---

# Learning Principle

My current focus is not only memorizing Python syntax.

The goal is to understand:

```text
What does this code mean?

Why is it used?

Where should it be used?

How does it connect with concepts I already know?

How will it connect with real data work later?
```

This learning diary documents that progression.
## 1. What Did I Learn Today?

Today I learned how Python exception handling, HTTP APIs, Ollama, a local LLM, and my Python modules connect together as one complete system.

The most important lesson was not only how to write the code, but also understanding:

```text
What is this component?
Why do I need it?
Where does it sit in the system?
What goes into it?
What comes out of it?
How does it connect to the other components?
```

---

### The Complete System I Built

My AI Sales Report Assistant works like this:

```text
sales.csv
    ↓
sales_analyzer.py
    ↓
Python dictionary containing calculated facts
    ↓
prompt_builder.py
    ↓
Text prompt
    ↓
llm_client.py
    ↓
requests library
    ↓
HTTP POST request
    ↓
Ollama API endpoint
    ↓
Ollama
    ↓
Qwen model
    ↓
Generated text
    ↓
Ollama API response
    ↓
llm_client.py
    ↓
app.py
    ↓
Terminal output
```

This helped me understand that each component has a different responsibility.

---

### What Is Qwen?

Qwen is the actual Large Language Model used in my project.

My model is:

```text
qwen3.5:4b
```

Qwen is responsible for understanding the prompt and generating the management report.

Conceptually:

```text
Prompt
    ↓
Qwen
    ↓
Generated language
```

Qwen is not:

```text
Python
requests library
API client
Ollama
```

Qwen is the actual AI model performing the language-generation work.

---

### What Is Ollama?

Ollama is not the LLM itself.

Ollama is software used to run and manage LLMs locally.

In my project:

```text
Ollama
→ runs/manages the local model

Qwen
→ actual model that generates the text
```

When I use:

```bash
ollama run qwen3.5:4b
```

the relationship is conceptually:

```text
Ollama
    ↓
Loads/runs Qwen
    ↓
Qwen becomes available for use
```

Ollama also provides a local API so that programs such as my Python application can communicate with the model.

---

### Why Did I Install Ollama?

Python cannot automatically communicate with a downloaded LLM just because a model file exists.

I needed software that could:

```text
Manage the model
Run the model
Receive requests
Send prompts to the model
Return generated responses
```

Ollama provides that layer.

So the architecture becomes:

```text
Python Application
        ↓
Ollama
        ↓
Qwen Model
```

Without something like Ollama, I would need another way to load and serve the model.

---

### Why Did I Download Qwen?

Installing Ollama does not mean the actual language model is already available.

The model must also be downloaded.

For this project I downloaded:

```text
qwen3.5:4b
```

The model contains the trained parameters that perform the language-generation work.

The relationship is:

```text
Ollama
→ software/runtime

Qwen
→ actual trained AI model
```

---

### Why Is a Local Model Large?

Large Language Models contain many trained parameters.

The model files have to exist somewhere.

With a local LLM:

```text
Model files
→ stored on my own computer
```

With a cloud LLM:

```text
Model files
→ stored on the provider's servers
```

Therefore, a local model uses:

```text
My disk space
My memory
My CPU/GPU resources
My electricity
```

while a cloud provider uses its own infrastructure.

---

### What Is the API in My Project?

The API is not `llm_client.py`.

The API is the interface exposed by Ollama.

My project uses this endpoint:

```text
http://localhost:11434/api/generate
```

Breakdown:

```text
http
→ communication protocol

localhost
→ my own computer

11434
→ port where the Ollama service is available

/api/generate
→ specific endpoint used for text generation
```

The API provides a defined way for my Python application to communicate with Ollama.

---

### What Is an API Endpoint?

An endpoint is a specific address for a particular API operation.

For example:

```text
/api/generate
```

is used for generation.

Conceptually:

```text
Server
    ↓
API
    ↓
Specific endpoint
```

The endpoint tells the client where a particular request should be sent.

---

### What Is `llm_client.py`?

`llm_client.py` is not the API.

It is my API client module.

Its responsibility is:

```text
Know where to send the request
Create the request
Send the request
Receive the response
Handle API-related errors
Return the generated result
```

Conceptually:

```text
llm_client.py
→ client-side code

Ollama API
→ server-side interface
```

---

### What Is the `requests` Library?

I use:

```python
import requests
```

`requests` is a Python library for sending HTTP requests.

It does not run the LLM.

It does not generate the report.

Its job is communication.

Conceptually:

```text
Python
    ↓
requests
    ↓
HTTP request
    ↓
Server/API
```

In my project:

```python
response = requests.post(
    url,
    json=payload,
    timeout=30
)
```

means:

```text
Send this data
→ to this URL
→ using HTTP POST
→ wait up to the configured timeout
```

---

### What Is the Payload?

The payload is the data I send to the API.

Example:

```python
payload = {
    "model": "qwen3.5:4b",
    "prompt": prompt,
    "stream": False,
    "think": False
}
```

This tells Ollama:

```text
Which model?
→ qwen3.5:4b

What should the model process?
→ prompt

Should the response stream in chunks?
→ False

Should thinking mode be used/exposed?
→ False
```

The payload begins as a Python dictionary.

Using:

```python
json=payload
```

allows `requests` to send it as JSON.

Flow:

```text
Python dictionary
        ↓
JSON
        ↓
HTTP request
        ↓
Ollama API
```

---

### What Does `stream` Mean?

```python
"stream": False
```

controls how the generated response is returned.

Conceptually:

```text
stream = True
→ response can arrive piece by piece

stream = False
→ wait for the complete response
```

For this project, I wanted a complete sales report at once.

---

### What Does `think` Mean?

```python
"think": False
```

is related to the model's thinking/reasoning mode.

For this application I want the final report rather than extra thinking output.

So:

```text
think = False
→ return the final generated answer for the application
```

---

### What Happens After I Send the API Request?

This was one of the most important connections I learned.

When my Python code executes:

```python
response = requests.post(
    url,
    json=payload,
    timeout=30
)
```

the conceptual flow is:

```text
Python application
        ↓
requests library
        ↓
HTTP POST request
        ↓
Ollama API
        ↓
Ollama reads the payload
        ↓
Ollama sees:
model = qwen3.5:4b
        ↓
Ollama sends the prompt to Qwen
        ↓
Qwen generates text
        ↓
Ollama creates an API response
        ↓
HTTP response
        ↓
Python receives it
```

So the model is not directly communicating with my Python code.

Ollama sits between my application and the Qwen model.

---

### What Is the Response?

The variable:

```python
response
```

contains the HTTP response object.

It can contain information such as:

```text
Status code
Headers
Response body
JSON data
```

To get the JSON body as Python data:

```python
response_data = response.json()
```

Then I can access the generated text:

```python
response_data["response"]
```

Flow:

```text
HTTP Response Object
        ↓
response.json()
        ↓
Python dictionary
        ↓
["response"]
        ↓
Generated LLM text
```

---

### What Is `app.py` Doing?

`app.py` connects all the modules.

It acts as the main orchestrator.

Example flow:

```python
data = analyze_sales("sales.csv")
```

means:

```text
sales_analyzer.py
→ calculate the sales facts
```

Then:

```python
prompt = build_prompt(data)
```

means:

```text
prompt_builder.py
→ turn the calculated facts into a prompt
```

Then:

```python
report = send_api_request(prompt)
```

means:

```text
llm_client.py
→ send the prompt to the LLM service
→ receive the generated answer
→ return it
```

Finally:

```python
print(report)
```

displays the report.

---

### Separation of Responsibilities

The project is divided into modules because each module has a different responsibility.

```text
sales_analyzer.py
→ Data calculation

prompt_builder.py
→ Prompt creation

llm_client.py
→ API communication

app.py
→ Connect everything together
```

This is easier to understand and maintain than placing all logic in one large file.

---

### Deterministic Python vs Generative AI

One important design decision was:

```text
Python calculates the facts.

LLM writes the natural-language report.
```

For example:

```text
Python calculates:
Total sales = 16700

LLM receives:
Total sales: 16700

LLM writes:
Total sales: 16700
```

I do not need the LLM to calculate values that Python can calculate reliably.

This reduces unnecessary hallucination and makes the application more predictable.

---

### Exception Handling

I learned how to prevent programs from crashing when errors occur.

Basic structure:

```python
try:
    # risky code

except SomeError:
    # handle the error
```

---

### `ValueError`

Example:

```python
number = int("hello")
```

causes:

```text
ValueError
```

because `"hello"` cannot be converted into an integer.

---

### Multiple Exception Types

Different errors can be handled differently.

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Number cannot be zero.")
```

---

### `else`

`else` runs only if no exception occurs.

```python
try:
    ...
except:
    ...
else:
    ...
```

Concept:

```text
Success
→ else runs

Error
→ matching except runs
→ else does not run
```

---

### `finally`

`finally` runs whether an error occurs or not.

Concept:

```text
Success
→ finally runs

Error
→ finally still runs
```

---

### API Connection Error

For API communication I learned:

```python
requests.exceptions.ConnectionError
```

This can happen when the client cannot connect to the server.

Concept:

```text
Python
→ tries to reach API
→ API/server unavailable
→ ConnectionError
```

---

### Connection Error vs HTTP Error

These are different.

```text
ConnectionError
→ server could not be reached
```

But:

```text
404
→ server was reached
→ requested endpoint was not found
```

This distinction is important.

---

### HTTP Status Codes

Some common HTTP status codes:

```text
200 → Success
400 → Bad Request
404 → Not Found
500 → Server Error
```

A status code means the server sent a response.

---

### `raise_for_status()`

I learned:

```python
response.raise_for_status()
```

This checks whether the HTTP status represents an error.

Concept:

```text
2xx
→ continue

4xx / 5xx
→ raise HTTPError
```

---

### Timeout

I used:

```python
timeout=30
```

A timeout prevents the application from waiting forever for the server.

Possible exception:

```python
requests.exceptions.Timeout
```

---

### Requests Exception Hierarchy

The `requests` library contains its own exception classes.

Examples:

```text
RequestException
├── ConnectionError
├── Timeout
└── HTTPError
```

These are related to the `requests` library.

They are different from Python built-in exceptions such as:

```text
ValueError
ZeroDivisionError
FileNotFoundError
```

---

### Why Specific Exceptions Come First

Example:

```python
except requests.exceptions.ConnectionError:
    ...

except requests.exceptions.Timeout:
    ...

except requests.exceptions.HTTPError:
    ...

except requests.exceptions.RequestException:
    ...
```

Rule:

```text
Specific exceptions first
        ↓
General exception last
```

This allows different problems to have different responses.

---

### `print()` vs `return`

I reviewed an important function concept.

```python
print(value)
```

means:

```text
Display this value.
```

But:

```python
return value
```

means:

```text
Send this value back to the caller.
```

If a Python function does not explicitly return a value:

```text
Python automatically returns None
```

This explained why I previously saw:

```text
None
```

after the generated report.

---

### Why Did We Use a Local LLM Instead of a Cloud API?

We could have used a cloud LLM API.

A cloud API was technically possible.

However, we intentionally used a local Ollama setup first so I could learn the main API concepts without adding many cloud-specific concepts at the same time.

With local Ollama:

```text
Python
    ↓
HTTP
    ↓
localhost
    ↓
Ollama API
    ↓
Qwen
```

This allowed me to focus on:

```text
Client
Server
Endpoint
POST
Payload
JSON
Response
Status code
Timeout
Exception handling
```

without immediately needing:

```text
API keys
Authentication
Cloud billing
Rate limits
Provider accounts
Secret management
Cloud security
```

---

### Could I Use a Cloud LLM API?

Yes.

The architecture would still be similar.

Current local version:

```text
Python Application
        ↓
requests
        ↓
Ollama API on localhost
        ↓
Qwen on my computer
```

Cloud version:

```text
Python Application
        ↓
requests / provider SDK
        ↓
Internet
        ↓
Cloud API
        ↓
Cloud-hosted model
```

The fundamental API ideas stay the same.

---

### Would Only the URL Change?

No.

The URL would change, but other things could also change.

Current local endpoint:

```text
http://localhost:11434/api/generate
```

Cloud might use something conceptually like:

```text
https://api.provider.com/...
```

But cloud integration may also require:

```text
Authentication
API key
Authorization headers
Provider-specific model name
Different payload structure
Different response structure
Rate-limit handling
Retries
Cost monitoring
Security
```

So moving from local to cloud is not simply changing one URL.

---

### What Would I Need to Learn for a Cloud LLM API?

The next important concepts would be:

```text
API keys
Authentication
HTTP headers
Environment variables
401 authentication errors
429 rate-limit errors
Retries
Provider-specific API documentation
Token/usage cost
Secret management
Security and privacy
```

These would build on top of the API concepts I already learned.

---

### Why Is This Local Project Useful for Cloud API Work?

Because the core concepts transfer.

I already understand:

```text
Client
Server
Endpoint
HTTP
POST
JSON
Payload
Response
Status code
Timeout
Exception handling
```

For cloud usage I would add:

```text
Authentication
Security
Provider-specific schema
Rate limits
Retries
Cost
```

So I would not be starting from zero.

---

## 2. What Did I Do Today?

Today I first practiced exception handling separately before applying it to the portfolio project.

I practiced:

```text
try
except
else
finally
ValueError
ZeroDivisionError
```

I then practiced API-specific errors:

```text
ConnectionError
Timeout
HTTPError
RequestException
```

I deliberately called a wrong Ollama endpoint and received:

```text
404
```

This helped me understand the difference between:

```text
Connection failure
```

and:

```text
Server response with an HTTP error
```

I practiced:

```python
response.raise_for_status()
```

and saw how a `404` response could become an `HTTPError`.

I also practiced a successful Ollama request and received:

```text
200
```

Then I created a POST request with a payload:

```python
payload = {
    "model": "qwen3.5:4b",
    "prompt": "Say hello in one sentence.",
    "stream": False,
    "think": False
}
```

I sent it using:

```python
requests.post()
```

and successfully received:

```text
Hello! It's great to meet you.
```

After learning these concepts separately, I applied them to the AI Sales Report Assistant.

I added:

```text
Timeout handling
HTTP status checking
Connection error handling
HTTP error handling
General request error handling
```

I also corrected the difference between:

```text
print()
```

and:

```text
return
```

so that `llm_client.py` returns the generated report to `app.py` instead of causing `None` to appear.

I also improved my understanding of the full project architecture:

```text
CSV
→ Python calculations
→ Prompt
→ API client
→ Ollama API
→ Qwen
→ Response
→ Final report
```

Finally, I prepared the project for GitHub and created a `.gitignore` file containing:

```text
.DS_Store
__pycache__/
*.pyc
.venv/
.env
```

---

## 3. Interview Questions & Answers

### What is the actual LLM in your project?

The actual LLM is Qwen.

I used:

```text
qwen3.5:4b
```

Qwen receives the prompt and generates the natural-language report.

---

### What is Ollama?

Ollama is software used to run and manage LLMs locally.

In my project, Ollama runs the Qwen model and exposes a local API that my Python application can call.

---

### Is Ollama the model?

No.

The distinction is:

```text
Ollama
→ software/runtime used to run and expose the model

Qwen
→ actual Large Language Model
```

---

### Why did you install Ollama?

I needed a way to run the model locally and expose it through an API that my Python application could communicate with.

Ollama provides that layer.

---

### Why did you download Qwen separately?

Ollama is the runtime, but Qwen is the actual model.

The model contains the trained parameters needed for language generation, so the model must also be available locally.

---

### What is the API in your project?

The project uses the local Ollama API.

The generation endpoint is:

```text
http://localhost:11434/api/generate
```

---

### Is `llm_client.py` the API?

No.

`llm_client.py` is my API client code.

It sends requests to the Ollama API and processes the responses.

---

### What is the `requests` library used for?

The `requests` library allows my Python code to send HTTP requests.

In this project I use it to send an HTTP POST request to the Ollama API.

---

### What happens when your Python application sends a prompt?

The flow is:

```text
Python
→ requests
→ HTTP POST request
→ Ollama API
→ Ollama sends prompt to Qwen
→ Qwen generates text
→ Ollama returns JSON response
→ Python reads the response
```

---

### What is a payload?

A payload is the data sent with the API request.

In my project it contains:

```text
model
prompt
stream
think
```

---

### What is JSON used for?

JSON is used to exchange structured data between my Python application and the API.

My Python dictionary is sent as JSON, and the API returns JSON data.

---

### What does `response.json()` do?

It converts the JSON response body into Python data.

Then I can access the generated text using:

```python
response_data["response"]
```

---

### What is the difference between a ConnectionError and a 404?

A `ConnectionError` means the client could not reach the server.

A `404` means the server was reached successfully, but the requested endpoint or resource was not found.

---

### What does `raise_for_status()` do?

It checks the HTTP response status.

If the response contains a 4xx or 5xx error, it raises an `HTTPError`.

---

### Why did you add a timeout?

A timeout prevents the application from waiting forever for a server response.

Example:

```python
timeout=30
```

---

### Why do you handle `RequestException` last?

Because it is a more general request-related exception.

More specific exceptions should be checked first:

```text
ConnectionError
Timeout
HTTPError
RequestException
```

---

### Why does Python calculate the sales metrics instead of the LLM?

Python calculations are deterministic and reliable.

The LLM is used for natural-language generation.

My architecture is:

```text
Python
→ calculates facts

LLM
→ writes the report
```

---

### Why did you use a local LLM instead of a cloud API?

I wanted to first learn the core API workflow:

```text
HTTP
POST
JSON
Payload
Response
Status codes
Timeout
Error handling
```

without immediately adding:

```text
API keys
Authentication
Rate limits
Cloud billing
Secret management
```

The same core API concepts can later be transferred to a cloud LLM API.

---

### Could this project use a cloud LLM?

Yes.

The main application architecture could remain similar.

Instead of:

```text
Python
→ Ollama local API
→ local Qwen
```

it could become:

```text
Python
→ cloud API
→ cloud-hosted LLM
```

The main changes would happen mostly in the LLM client layer.

---

### What would you need to change for a cloud LLM API?

I would first read the provider's API documentation.

Then I would identify:

```text
Cloud API endpoint
Authentication method
API key requirements
Headers
Model ID
Request schema
Response schema
Rate limits
Errors
Pricing
```

I would then update my client code accordingly.

---

### Would you hardcode an API key in your Python file?

No.

I would store sensitive credentials outside the source code, for example using environment variables.

I would also make sure secret files such as:

```text
.env
```

are excluded from Git using:

```text
.gitignore
```

---

### Explain your project in one answer.

My application reads sales data from a CSV file and calculates the required business metrics using Python. It then builds a structured prompt and passes it to an API client module. The client uses the Python `requests` library to send an HTTP POST request to Ollama's local API. Ollama runs the Qwen language model, sends the prompt to the model, and returns the generated text as a JSON response. My Python application extracts that generated response and displays the final management sales report.

---

## 4. Summary — Mistakes & Corrections

### Mistake: Thinking Ollama and Qwen were the same thing

Correction:

```text
Ollama
→ software/runtime

Qwen
→ actual LLM
```

Ollama runs and manages the model.

Qwen performs the language generation.

---

### Mistake: Thinking `llm_client.py` was the API

Correction:

```text
llm_client.py
→ API client code

Ollama API
→ interface being called

/api/generate
→ API endpoint
```

---

### Mistake: Learning API code without connecting the architecture

Correction:

I should understand the full relationship:

```text
Python
→ requests
→ HTTP
→ API endpoint
→ Ollama
→ Qwen
→ response
→ Python
```

The syntax is only one part of the system.

---

### Mistake: Exception spelling

Incorrect:

```python
ValueErrror
```

Correct:

```python
ValueError
```

---

### Mistake: Incorrect dictionary syntax

Incorrect:

```python
"model": "qwen3.5:4b"
"prompt": "Hello"
```

Correct:

```python
"model": "qwen3.5:4b",
"prompt": "Hello",
```

Dictionary items need commas between them.

---

### Mistake: Incorrect `stream` key

Incorrect:

```python
"stream:": False
```

Correct:

```python
"stream": False
```

The colon belongs between the key and value.

---

### Mistake: Confusing ConnectionError with HTTP errors

Correction:

```text
ConnectionError
→ server could not be reached

404 / 500
→ server was reached and returned an error response
```

---

### Mistake: Printing instead of returning

If a function only does:

```python
print(response_data["response"])
```

but the caller expects a returned value, the function eventually returns:

```text
None
```

Correct:

```python
return response_data["response"]
```

---

### Mistake: Thinking cloud migration only means changing the URL

Correction:

A cloud migration may require:

```text
Remote URL
Authentication
API key
Headers
Different payload
Different response parsing
Rate-limit handling
Retries
Security
Cost monitoring
```

The core API concepts remain similar, but cloud integration adds additional responsibilities.

---

### Main Learning Principle

For future technologies, I should not learn only the syntax.

I should ask:

```text
1. What is it?

2. Why do I need it?

3. Where does it sit in the system?

4. What goes into it?

5. What comes out of it?

6. How does it connect to what I already know?
```

Then the learning process should be:

```text
Understand the concept
        ↓
Understand the architecture
        ↓
Learn the syntax
        ↓
Practice separately
        ↓
Debug mistakes
        ↓
Rebuild from memory
        ↓
Apply it to a portfolio project
```

This helps me understand the complete system instead of only memorizing code.


# Daily Learning — Python Day 8 + SQL Day 1 & 2

## 1. What Did I Learn Today?

### Python Day 8 — Data Cleaning

Today I completed Python Day 8: Data Cleaning.

Data Cleaning is the process of finding and fixing problems in data before analysis.

I learned these main data-quality problems:

- Missing values
- Invalid values
- Inconsistent formatting
- Duplicate records
- Incorrect data types
- Dirty data
- Data quality

### Missing Values

A missing value means an expected value is absent.

Example:

```python
{"name": "Rafi", "city": "", "sales": 1400}
```

Here, the `city` value is missing.

### Invalid Values

An invalid value is present, but it breaks an expected rule or business rule.

Example:

```python
{"name": "Sara", "sales": -500}
```

`-500` is an integer, so the data type is correct, but the value may be invalid according to the business rule.

Important distinction:

```text
Incorrect data type
≠
Invalid value

"3200"
→ string
→ incorrect type for numerical calculation

-500
→ integer
→ correct type
→ but possibly invalid business value
```

### Inconsistent Formatting

Inconsistent formatting means the same kind of data is stored in different formats.

Example:

```text
Helsinki
helsinki
HELSINKI
 Helsinki 
```

I practiced removing extra whitespace with:

```python
record["city"] = record["city"].strip()
```

Important connection:

```text
record["city"].strip()
→ creates a cleaned version

record["city"] = record["city"].strip()
→ creates the cleaned version and saves it back
```

### Incorrect Data Types

CSV values are normally read as strings.

Example:

```text
"3200"
→ str
```

For numerical calculations, I may need:

```python
record["sales"] = int(record["sales"])
```

Result:

```text
"3200"
→ 3200
→ str becomes int
```

### Duplicate Records

Two identical-looking rows should not automatically be deleted.

They may represent:

- an accidental duplicate
- two separate valid transactions

More information may be needed, such as:

- transaction ID
- order number
- timestamp
- confirmation from the business source

So identical-looking records should initially be treated as possible duplicates until there is enough evidence.

### Cleaning vs Detection

I learned the difference between cleaning data and detecting a problem.

```text
Cleaning
→ actually changes/fixes the data

Detection
→ identifies that a problem exists
```

Example of cleaning:

```python
record["city"] = record["city"].strip()
```

Example of detection:

```python
if record["sales"] < 0:
    print("Invalid sales value")
```

The second example detects the problem but does not automatically decide how to correct it.

### Data Cleaning Workflow

```text
Raw data
↓
Identify problems
↓
Clean / validate data
↓
Reliable data
↓
Analysis
↓
Report / Dashboard
↓
Business decision
```

Important principle:

> Correct calculations performed on bad data can still produce incorrect or misleading business results.

---

### SQL Foundations

After completing Python Day 8, I started SQL.

SQL stands for **Structured Query Language**.

SQL is used to communicate with relational databases and work with structured data.

### Database

A database is an organized collection of data that can be stored, managed, and retrieved.

### Table

A table stores related data in rows and columns.

### Row

A row usually represents one complete record.

### Column

A column represents one type or field of information.

Connection to Python and CSV:

```text
Python dictionary
→ one record

List of dictionaries
→ multiple records

CSV row
→ one record

SQL row
→ one record

SQL table
→ multiple records
```

### Query

A query is an instruction or request sent to a database to retrieve or work with data.

---

### SELECT

`SELECT` decides which columns or calculated results should appear.

```sql
SELECT name, sales
FROM sales;
```

`*` means all columns:

```sql
SELECT *
FROM sales;
```

### FROM

`FROM` specifies which table SQL should use.

```text
SELECT
→ which columns?

FROM
→ which table?
```

### WHERE

`WHERE` filters individual rows using conditions.

```sql
SELECT name, sales
FROM sales
WHERE sales > 3000;
```

Connection to Python:

```text
Python if
→ checks a condition

SQL WHERE
→ filters rows using a condition
```

### Comparison Operators

```text
=   equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to
<>  not equal to
```

Important difference:

```text
Python equality → ==
SQL equality    → =
```

### AND

`AND` means all connected conditions must be true.

```sql
WHERE sales > 3000
AND city = 'Helsinki'
```

### OR

`OR` means at least one condition must be true.

```sql
WHERE city = 'Espoo'
OR city = 'Turku'
```

### IN

`IN` is a cleaner way to check several possible values for the same column.

```sql
WHERE city IN ('Helsinki', 'Espoo', 'Turku')
```

This is similar to:

```sql
WHERE city = 'Helsinki'
OR city = 'Espoo'
OR city = 'Turku'
```

### BETWEEN

`BETWEEN` checks whether a value is inside a range.

```sql
WHERE sales BETWEEN 2000 AND 4000
```

`BETWEEN` is inclusive.

```text
sales >= 2000
AND
sales <= 4000
```

The lower and upper boundary values are included.

---

### ORDER BY

`ORDER BY` sorts query results.

```text
ASC
→ lowest to highest
→ A to Z

DESC
→ highest to lowest
→ Z to A
```

Example:

```sql
SELECT name, sales
FROM sales
ORDER BY sales DESC;
```

### LIMIT

`LIMIT` restricts how many rows are returned.

```sql
SELECT name, sales
FROM sales
ORDER BY sales DESC
LIMIT 3;
```

Important connection:

```text
ORDER BY
→ decides which rows come first

LIMIT
→ decides how many rows are returned
```

This can be used for Top-N analysis.

---

### Aggregate Functions

Aggregate functions summarize multiple values.

```text
SUM()
→ total

MIN()
→ lowest value

MAX()
→ highest value

AVG()
→ average

COUNT()
→ count
```

Connection to Python:

```text
Python        SQL

sum()         SUM()
min()         MIN()
max()         MAX()
len()         COUNT()
average       AVG()
```

### SUM()

```sql
SELECT SUM(sales)
FROM sales;
```

Returns the total sales.

### MIN()

```sql
SELECT MIN(sales)
FROM sales;
```

Returns the lowest sales value.

### MAX()

```sql
SELECT MAX(sales)
FROM sales;
```

Returns the highest sales value.

### AVG()

```sql
SELECT AVG(sales)
FROM sales;
```

Conceptually:

```text
AVG(sales)
≈
SUM(sales) / COUNT(sales)
```

`AVG(column)` ignores `NULL` values in that column.

### COUNT(*)

```sql
SELECT COUNT(*)
FROM sales;
```

Counts all rows.

### COUNT(column_name)

```sql
SELECT COUNT(sales)
FROM sales;
```

Counts non-NULL values in the `sales` column.

Important distinction:

```text
COUNT(*)
→ counts rows

COUNT(column)
→ counts non-NULL values in that column
```

---

### GROUP BY

`GROUP BY` puts rows with the same value into groups so that aggregate functions can summarize each group.

Example:

```sql
SELECT city, SUM(sales)
FROM sales
GROUP BY city;
```

Conceptually:

```text
GROUP BY city
→ create one group per city

SUM(sales)
→ total sales inside each city group
```

Important difference:

```text
GROUP BY
→ creates groups for aggregation

ORDER BY
→ sorts the result
```

### HAVING

`HAVING` filters grouped or aggregate results.

```sql
SELECT city, SUM(sales)
FROM sales
GROUP BY city
HAVING SUM(sales) > 7000;
```

Important distinction:

```text
WHERE
→ filters individual rows
→ before grouping / aggregation

HAVING
→ filters grouped / aggregate results
→ after aggregation
```

`HAVING` can also be used without `GROUP BY` when the entire result is treated as one aggregate group.

Example:

```sql
SELECT AVG(sales)
FROM sales
HAVING AVG(sales) > 3000;
```

---

### AS — Alias

`AS` gives a temporary readable name to a column or calculated result.

```sql
SELECT city, SUM(sales) AS total_sales
FROM sales
GROUP BY city;
```

`AS` does not permanently rename the database column.

---

### DISTINCT

`DISTINCT` returns unique values.

```sql
SELECT DISTINCT city
FROM sales;
```

Important distinction:

```text
DISTINCT
→ use when I only want unique values

GROUP BY
→ use when I want summaries for each category
```

Example:

```sql
SELECT DISTINCT product
FROM sales
WHERE city IN ('Helsinki', 'Turku');
```

---

## 2. What Did I Do Today?

I completed Python Day 8 Data Cleaning before starting SQL.

For Python Data Cleaning, I practiced:

- detecting missing values
- detecting invalid values
- identifying inconsistent formatting
- removing extra whitespace using `strip()`
- converting CSV strings to integers using `int()`
- saving cleaned values back into dictionaries
- identifying possible duplicate records
- distinguishing between detection and actual cleaning
- connecting CSV data cleaning to future pandas, SQL, and BI work

Example:

```python
for record in sales_data:
    record["city"] = record["city"].strip()
    record["sales"] = int(record["sales"])

    if record["city"] == "":
        print(f"Missing city for {record['name']}")

    if record["sales"] < 0:
        print(f"Invalid sales value for {record['name']}")
```

I then started SQL and practiced:

- `SELECT`
- `FROM`
- `WHERE`
- comparison operators
- `AND`
- `OR`
- `IN`
- `BETWEEN`
- `ORDER BY`
- `ASC`
- `DESC`
- `SUM()`
- `MIN()`
- `MAX()`
- `AVG()`
- `COUNT(*)`
- `COUNT(column)`
- `GROUP BY`
- `HAVING`
- `AS`
- `DISTINCT`
- `LIMIT`

I also practiced more difficult SQL business questions.

Example:

```sql
SELECT city, SUM(sales) AS total_sales
FROM sales
WHERE city IN ('Helsinki', 'Espoo', 'Turku')
GROUP BY city
HAVING SUM(sales) > 6000
ORDER BY SUM(sales) DESC;
```

I also practiced finding Top-N groups:

```sql
SELECT city, SUM(sales)
FROM sales
GROUP BY city
ORDER BY SUM(sales) DESC
LIMIT 2;
```

And lowest/highest sales for each city:

```sql
SELECT city,
       MIN(sales) AS lowest_sale,
       MAX(sales) AS highest_sale
FROM sales
GROUP BY city;
```

---

## 3. Interview Questions & Answers

### What is Data Cleaning?

Data Cleaning is the process of identifying and correcting data-quality problems before analysis.

### What is a missing value?

A missing value is an expected value that is absent.

### What is an invalid value?

An invalid value exists but does not follow the expected business rule or allowed range.

### What is inconsistent formatting?

Inconsistent formatting means the same kind of data is stored using different formats.

### What is the difference between detection and cleaning?

Detection identifies that a problem exists.

Cleaning actually changes or fixes the data.

### Why should duplicate-looking rows not automatically be deleted?

Because identical-looking rows may represent separate valid transactions. More information such as transaction ID, order ID, or timestamp may be needed.

### What is SQL?

SQL stands for Structured Query Language. It is used to communicate with relational databases and work with structured data.

### What is a database?

A database is an organized collection of data that can be stored, managed, and retrieved.

### What is a table?

A table stores related records in rows and columns.

### What is the difference between a row and a column?

A row represents one record.

A column represents one type or field of information.

### What does SELECT do?

`SELECT` specifies which columns or calculated results should appear.

### What does FROM do?

`FROM` specifies which table the query uses.

### What does WHERE do?

`WHERE` filters individual rows based on a condition.

### What is the difference between AND and OR?

`AND` requires all connected conditions to be true.

`OR` requires at least one condition to be true.

### What does IN do?

`IN` checks whether a value matches one of several possible values.

### What does BETWEEN do?

`BETWEEN` checks whether a value falls inside a range.

It is inclusive, so both boundary values are included.

### What does ORDER BY do?

`ORDER BY` sorts query results.

### What is the difference between ASC and DESC?

`ASC` sorts lowest to highest or A to Z.

`DESC` sorts highest to lowest or Z to A.

### What is an aggregate function?

An aggregate function summarizes multiple values into one result.

Examples:

- `SUM()`
- `AVG()`
- `MIN()`
- `MAX()`
- `COUNT()`

### What is the difference between COUNT(*) and COUNT(column)?

`COUNT(*)` counts all rows.

`COUNT(column)` counts only non-NULL values in that column.

### What does GROUP BY do?

`GROUP BY` creates groups of rows with matching values so aggregate functions can calculate summaries for each group.

### What is the difference between GROUP BY and ORDER BY?

`GROUP BY` creates groups for aggregation.

`ORDER BY` sorts query results.

### What is the difference between WHERE and HAVING?

`WHERE` filters individual rows before aggregation.

`HAVING` filters grouped or aggregate results after aggregation.

### What does DISTINCT do?

`DISTINCT` returns unique values or unique combinations of selected columns.

### What does AS do?

`AS` creates a temporary readable alias for a column or calculated result.

### What does LIMIT do?

`LIMIT` restricts the number of rows returned by a query.

---

## 4. Summary — Mistakes & Corrections

### Python Data Cleaning — print vs reassignment

This:

```python
print(record["city"].strip())
```

only displays the cleaned value.

This:

```python
record["city"] = record["city"].strip()
```

actually saves the cleaned value back into the dictionary.

### Invalid value vs incorrect data type

```text
-500
→ int
→ type is correct
→ value may be invalid

"3200"
→ str
→ wrong type for numerical calculation
```

### Duplicate records

Two identical-looking rows are not automatically duplicates.

I need more business context before deleting data.

---

### SQL — Using WHERE twice

Incorrect:

```sql
WHERE sales BETWEEN 2000 AND 4500
WHERE city IN ('Helsinki', 'Espoo')
```

Correct:

```sql
WHERE sales BETWEEN 2000 AND 4500
AND city IN ('Helsinki', 'Espoo')
```

### SQL — Text values need quotes

Incorrect:

```sql
city IN (Helsinki, Espoo)
```

Correct:

```sql
city IN ('Helsinki', 'Espoo')
```

### SQL — ASC vs DESC

```text
ASC
→ lowest to highest

DESC
→ highest to lowest
```

### SQL — GROUP BY with raw columns

Incorrect idea:

```sql
SELECT city, sales
FROM sales
GROUP BY city;
```

A city group may contain multiple sales values.

For summarized data:

```sql
SELECT city, AVG(sales)
FROM sales
GROUP BY city;
```

### SQL — WHERE vs HAVING

```text
WHERE
→ individual rows

HAVING
→ aggregate/group results
```

### SQL — DISTINCT with multiple columns

```sql
SELECT DISTINCT product, city, sales
```

returns unique combinations of all three selected columns.

If I only want unique product names:

```sql
SELECT DISTINCT product
FROM sales;
```

### SQL — Top-N needs sorting first

`LIMIT 2` alone does not mean top 2.

Correct pattern:

```sql
SELECT city, SUM(sales)
FROM sales
GROUP BY city
ORDER BY SUM(sales) DESC
LIMIT 2;
```

### Final SQL Mental Model

```text
FROM
→ which table?

WHERE
→ which individual rows?

GROUP BY
→ which groups?

Aggregate function
→ what summary calculation?

HAVING
→ which aggregated groups?

SELECT
→ what should appear in the result?

ORDER BY
→ how should the result be sorted?

LIMIT
→ how many rows should be returned?
```

Today I connected Python Data Cleaning with SQL and started moving from file-based data processing toward relational data analysis.
# SQL Learning — Schema, Keys, Relationships & Data Insertion

## 1. What Did I Learn Today?

Today I continued SQL learning with a short recall of previously learned concepts and then moved deeper into relational database structure.

---

### SQL Recall

I reviewed:

- `WHERE`
- `HAVING`
- `COUNT(*)`
- `COUNT(column)`
- `GROUP BY`
- `ORDER BY`
- `DISTINCT`
- `BETWEEN`
- `AVG()`
- `SUM()`
- `LIMIT`

Important recall:

```text
WHERE
→ filters individual rows
→ before grouping / aggregation

HAVING
→ filters grouped / aggregate results
→ after aggregation
```

```text
COUNT(*)
→ counts all rows

COUNT(column)
→ counts non-NULL values in that column
```

```text
GROUP BY
→ creates groups for aggregation

ORDER BY
→ sorts the result
```

I also successfully wrote:

```sql
SELECT city, AVG(sales) AS average_sales
FROM sales
WHERE sales > 2000
GROUP BY city
HAVING AVG(sales) > 3000
ORDER BY average_sales DESC;
```

This strengthened my understanding of the flow:

```text
WHERE
↓
GROUP BY
↓
Aggregate calculation
↓
HAVING
↓
ORDER BY
```

---

### NULL

`NULL` means:

```text
no known value
missing / unavailable value
```

Important distinction:

```text
NULL
≠ 0

NULL
≠ ''

NULL
≠ 'NULL'
```

To find missing values:

```sql
SELECT name
FROM sales
WHERE city IS NULL;
```

To find rows where the value exists:

```sql
SELECT name
FROM sales
WHERE city IS NOT NULL;
```

Important connection to `COUNT()`:

```text
COUNT(*)
→ counts every row

COUNT(sales)
→ ignores NULL values in sales
```

I also practiced counting missing values:

```sql
SELECT COUNT(*)
FROM sales
WHERE city IS NULL;
```

---

### LIKE

`LIKE` is used for text pattern matching.

Exact match:

```sql
WHERE city = 'Helsinki'
```

Pattern match:

```sql
WHERE name LIKE 'A%'
```

Important patterns:

```text
'A%'
→ starts with A

'%a'
→ ends with a

'%mi%'
→ contains mi anywhere
```

Example:

```sql
SELECT name
FROM sales
WHERE name LIKE 'S%';
```

This returns names that start with `S`.

---

### Wildcards: % and _

`%` means:

```text
zero or more characters
```

`_` means:

```text
exactly one character
```

Example:

```sql
WHERE name LIKE 'M_k_'
```

This can match:

```text
Mika
Mike
Mako
```

but not:

```text
Mikko
```

because `_` represents exactly one character.

---

### NOT

`NOT` reverses or excludes a condition.

Examples:

```sql
WHERE city NOT IN ('Helsinki', 'Turku')
```

means:

```text
all matching rows except Helsinki and Turku
```

```sql
WHERE sales NOT BETWEEN 2000 AND 4000
```

means:

```text
sales < 2000
OR
sales > 4000
```

Because `BETWEEN` is inclusive.

```sql
WHERE name NOT LIKE 'A%'
```

means:

```text
name does not start with A
```

Important distinction:

```sql
WHERE name NOT LIKE '%A%'
```

means:

```text
name does not contain A anywhere
```

---

### Primary Key

A Primary Key uniquely identifies a row in its own table.

Example:

```text
customer_id | name
------------|------
1           | Amina
2           | Rafi
3           | Amina
```

`name` cannot safely identify the record because names can repeat.

But:

```text
customer_id
```

can uniquely identify each row.

Important rules:

```text
PRIMARY KEY
→ unique
→ cannot be NULL
```

---

### Foreign Key

A Foreign Key is a column that references a key in another table.

Example:

```text
customers

customer_id | name
------------|------
1           | Amina
2           | Rafi
```

```text
orders

order_id | customer_id | amount
---------|-------------|-------
101      | 1           | 3200
102      | 2           | 1400
103      | 1           | 1800
```

Here:

```text
customers.customer_id
→ Primary Key

orders.customer_id
→ Foreign Key
```

The Foreign Key can repeat because one customer can have multiple orders.

Important distinction:

```text
Primary Key
→ identifies a row in its own table

Foreign Key
→ references a related row in another table
```

---

### JOIN Concept

I started learning how related tables are combined.

Example relationship:

```text
customers.customer_id
        ↕
orders.customer_id
```

An `INNER JOIN` returns only matching rows.

Example:

```sql
SELECT orders.order_id, customers.name, orders.amount
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

Important:

```text
ON
→ tells SQL which columns should match
```

I also learned the concept of `LEFT JOIN`.

```text
INNER JOIN
→ only matching rows

LEFT JOIN
→ all rows from the left table
→ matching rows from the right table
→ missing right-side match becomes NULL
```

However, I noticed an important conceptual gap:

> How does SQL know which column is a Primary Key and which one is a Foreign Key?

Because of that question, I paused deeper JOIN learning and went back to understand table schemas and key definitions properly.

---

### LEFT / RIGHT vs Primary / Foreign Key

This was an important distinction.

```text
LEFT / RIGHT
→ position of tables inside a query

PRIMARY KEY / FOREIGN KEY
→ relationship defined in the database schema
```

A Primary Key does not always need to appear on the right side of a JOIN.

A Foreign Key does not always need to appear on the left side.

The table order can change without changing the key relationship.

---

### Table Schema

A schema is the structure or blueprint of a database table.

It defines things such as:

```text
table name
columns
data types
constraints
Primary Keys
Foreign Keys
relationships
```

Example:

```text
customers

customer_id
→ integer
→ Primary Key

name
→ text

city
→ text
```

Important distinction:

```text
Schema
→ describes how data should be structured

Data
→ actual values stored inside that structure
```

---

### Schema Connection to Python Class

A table schema is conceptually similar to the structural part of a Python class.

```text
Python                     SQL

Class                      Table schema
Attribute                  Column
Object                     Row / record
Attribute value            Field value
```

But they are not exactly the same.

A Python class can contain:

```text
methods
behavior
logic
```

A table schema mainly defines:

```text
columns
data types
constraints
keys
relationships
```

---

### SQL Data Types

I learned three basic SQL data types:

```text
INT
→ whole numbers

VARCHAR(...)
→ text

DECIMAL(...)
→ decimal numbers
```

Connection to Python:

```text
Python              SQL

int                 INT
str                 VARCHAR
decimal number      DECIMAL
```

---

### VARCHAR(n)

Example:

```sql
name VARCHAR(100)
```

means:

```text
name
→ column name

VARCHAR
→ text data type

100
→ maximum number of characters
```

Important:

```text
VARCHAR(100)
```

does not mean the value must contain exactly 100 characters.

It means the maximum allowed length is 100 characters.

Example:

```sql
city VARCHAR(50)
```

means the city column can store text up to 50 characters.

---

### DECIMAL(p, s)

Example:

```sql
price DECIMAL(8, 2)
```

means:

```text
8
→ total number of digits

2
→ digits after the decimal point

8 - 2 = 6
→ maximum digits before the decimal point
```

Example valid value:

```text
999999.99
```

Important connection:

```text
INT
→ whole numbers

DECIMAL
→ decimal values
```

For financial values such as price, salary, cost, and amount, `DECIMAL` is an important data type.

---

### CREATE TABLE

`CREATE TABLE` creates a new table structure.

General structure:

```sql
CREATE TABLE table_name (
    column_name data_type,
    column_name data_type
);
```

I successfully created:

```sql
CREATE TABLE products(
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(8, 2)
);
```

Important:

```text
CREATE TABLE
→ creates structure

It does not automatically insert rows.
```

---

### PRIMARY KEY Inside CREATE TABLE

I learned how the database actually knows that a column is a Primary Key.

Example:

```sql
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(8, 2)
);
```

Here:

```text
product_id
→ column name

INT
→ data type

PRIMARY KEY
→ constraint / rule
```

This tells the database that `product_id` uniquely identifies each product.

---

### FOREIGN KEY Inside CREATE TABLE

I then learned how the relationship between tables is actually defined.

Parent table:

```sql
CREATE TABLE customers(
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

Related table:

```sql
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(8, 2),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
```

Meaning:

```text
orders.customer_id
→ Foreign Key

REFERENCES customers(customer_id)
→ points to customers.customer_id
```

So the database schema now knows:

```text
customers.customer_id
→ Primary Key

orders.customer_id
→ Foreign Key
→ references customers.customer_id
```

This answered my earlier JOIN question.

SQL does not guess Primary Keys and Foreign Keys based on which table appears on the left or right side.

They are defined in the schema.

---

### Referential Integrity

Referential Integrity means:

> A Foreign Key reference should point to a record that actually exists.

বাংলায়:

> যাকে reference করছি, সে যেন সত্যিই parent table-এ exists করে।

Example:

```text
customers.customer_id

1
2
```

This order is valid:

```text
customer_id = 2
```

because customer 2 exists.

This is invalid:

```text
customer_id = 99
```

because customer 99 does not exist.

Mental model:

```text
Referential Integrity
→ Foreign Key reference must remain valid
```

Important distinction:

```text
NOT NULL check
→ is there a value?

Foreign Key check
→ does that referenced value actually exist?
```

---

### INSERT INTO

`INSERT INTO` adds actual rows to a table.

General structure:

```sql
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);
```

Example:

```sql
INSERT INTO customers(customer_id, name)
VALUES(2, 'Rafi');
```

Important connection:

```text
CREATE TABLE
→ create structure

INSERT INTO
→ add actual data

SELECT
→ retrieve data
```

I also inserted a row containing a valid Foreign Key:

```sql
INSERT INTO orders(order_id, customer_id, amount)
VALUES(101, 2, 1400.50);
```

This is valid because:

```text
customer_id = 2
```

already exists in the `customers` table.

---

## 2. What Did I Do Today?

I started with SQL Day 1–2 blank-screen recall.

I successfully recalled:

- `WHERE` vs `HAVING`
- `COUNT(*)` vs `COUNT(column)`
- `GROUP BY` vs `ORDER BY`
- `DISTINCT`
- `BETWEEN`
- aggregate functions
- Top-N queries
- filtering before aggregation

I successfully wrote:

```sql
SELECT city, AVG(sales) AS average_sales
FROM sales
WHERE sales > 2000
GROUP BY city
HAVING AVG(sales) > 3000
ORDER BY average_sales DESC;
```

I then learned and practiced:

- `NULL`
- `IS NULL`
- `IS NOT NULL`
- `LIKE`
- `%`
- `_`
- `NOT IN`
- `NOT BETWEEN`
- `NOT LIKE`
- Primary Key
- Foreign Key
- basic `INNER JOIN`
- basic `LEFT JOIN`
- table schema
- schema vs data
- connection between SQL schema and Python classes
- `INT`
- `VARCHAR`
- `DECIMAL`
- `VARCHAR(n)`
- `DECIMAL(p, s)`
- `CREATE TABLE`
- `PRIMARY KEY` constraint
- `FOREIGN KEY` constraint
- `REFERENCES`
- referential integrity
- `INSERT INTO`

I successfully created:

```sql
CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(8, 2)
);
```

I also created a related table:

```sql
CREATE TABLE orders(
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount DECIMAL(8, 2),

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);
```

I inserted data:

```sql
INSERT INTO customers(customer_id, name)
VALUES(2, 'Rafi');
```

and:

```sql
INSERT INTO orders(order_id, customer_id, amount)
VALUES(101, 2, 1400.50);
```

Most importantly, I connected several concepts into one system:

```text
Database
↓
Table
↓
Schema
↓
Columns + Data Types
↓
Constraints
↓
Primary Key
↓
Foreign Key
↓
Relationship between tables
↓
INSERT actual data
↓
JOIN related data
```

---

## 3. Interview Questions & Answers

### What is NULL in SQL?

`NULL` represents a missing, unknown, or unavailable value.

It is not the same as `0`, an empty string, or the text `'NULL'`.

### How do you check for NULL?

Use:

```sql
IS NULL
```

or:

```sql
IS NOT NULL
```

Example:

```sql
WHERE city IS NULL
```

### What is LIKE used for?

`LIKE` is used for text pattern matching.

Example:

```sql
WHERE name LIKE 'A%'
```

returns names starting with `A`.

### What does % mean in LIKE?

`%` represents zero or more characters.

### What does _ mean in LIKE?

`_` represents exactly one character.

### What is a Primary Key?

A Primary Key uniquely identifies each row in a table.

It must be unique and cannot be NULL.

### What is a Foreign Key?

A Foreign Key is a column that references a key in another table and helps establish a relationship between tables.

### Can a Foreign Key repeat?

Yes.

For example, several orders can belong to the same customer.

### What is a table schema?

A table schema defines the structure of a table, including columns, data types, constraints, and relationships.

### What is the difference between schema and data?

Schema defines how data should be structured.

Data is the actual information stored inside that structure.

### What is INT?

`INT` is a data type used for whole numbers.

### What is VARCHAR?

`VARCHAR` is a variable-length text data type.

Example:

```sql
VARCHAR(100)
```

means the value can contain up to 100 characters.

### What does DECIMAL(8, 2) mean?

It allows up to 8 total digits, with 2 digits after the decimal point.

Therefore, up to 6 digits can appear before the decimal point.

### What does CREATE TABLE do?

`CREATE TABLE` creates a new table structure in a database.

### What does INSERT INTO do?

`INSERT INTO` adds new rows to an existing table.

### What does REFERENCES mean?

`REFERENCES` identifies the table and column that a Foreign Key points to.

Example:

```sql
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id)
```

### What is referential integrity?

Referential integrity means Foreign Key references remain valid.

A child record should not reference a parent record that does not exist.

### What is the difference between NOT NULL and a Foreign Key?

`NOT NULL` checks whether a value exists.

A Foreign Key checks whether the referenced value exists in the related table.

### What is the difference between Primary/Foreign Key and LEFT/RIGHT?

Primary Key and Foreign Key describe the relationship defined in the schema.

LEFT and RIGHT describe table positions inside a query.

### What is an INNER JOIN?

An `INNER JOIN` returns rows that have matching values in both related tables.

### What is a LEFT JOIN?

A `LEFT JOIN` keeps all rows from the left table and adds matching values from the right table.

If there is no right-side match, the right-side values become `NULL`.

---

## 4. Summary — Mistakes & Corrections

### COUNT(column)

My first explanation was:

```text
COUNT(sales)
→ counts the sales column
```

More precise:

```text
COUNT(sales)
→ counts non-NULL values in the sales column
```

---

### NOT LIKE Pattern

I initially interpreted:

```sql
WHERE name NOT LIKE 'A%'
```

as:

```text
name has no A
```

Correction:

```text
'A%'
→ starts with A

NOT LIKE 'A%'
→ does not start with A
```

To exclude names containing `A` anywhere:

```sql
WHERE name NOT LIKE '%A%'
```

---

### INNER JOIN Syntax

I initially wrote:

```sql
FROM orders
INNER JOIN
ON orders.customer_id = customers.customer_id;
```

I forgot to specify the table after `INNER JOIN`.

Correct:

```sql
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```

---

### Primary Key / Foreign Key vs Left / Right

Initially, it was easy to think:

```text
Foreign Key
→ left side

Primary Key
→ right side
```

Correction:

This is not a rule.

```text
LEFT / RIGHT
→ query position

PRIMARY KEY / FOREIGN KEY
→ schema relationship
```

Tables can switch positions without changing which column is the Primary Key or Foreign Key.

---

### CREATE TABLE Column Names

While practicing, I wrote:

```sql
price_price
```

instead of:

```sql
price
```

and later:

```sql
name
```

instead of:

```sql
product_name
```

This reminded me that SQL syntax may be correct while the schema can still differ from the requested design.

---

### VARCHAR Length

I initially used:

```sql
VARCHAR(50)
```

when the requested schema required:

```sql
VARCHAR(100)
```

The number defines the maximum allowed characters.

---

### FOREIGN KEY Syntax

I initially wrote:

```sql
REFERENCE customers(customer_id)
```

Correct keyword:

```sql
REFERENCES customers(customer_id)
```

---

### Missing Comma in CREATE TABLE

I initially forgot the comma before the table-level Foreign Key constraint.

Incorrect:

```sql
amount DECIMAL(8, 2)

FOREIGN KEY ...
```

Correct:

```sql
amount DECIMAL(8, 2),

FOREIGN KEY ...
```

---

### Foreign Key vs NULL

I initially thought that because:

```text
customer_id = 99
```

is not `NULL`, it might be acceptable.

Correction:

```text
NOT NULL
→ checks whether a value exists

FOREIGN KEY
→ checks whether the referenced value exists
```

So:

```text
customer_id = 99
```

can still be invalid if customer `99` does not exist.

---

### Final Mental Model

```text
CREATE TABLE
→ define the structure

Column
→ named field in the table

Data Type
→ what type of value the column stores

PRIMARY KEY
→ uniquely identify a row

FOREIGN KEY
→ reference a row in another table

REFERENCES
→ define what the Foreign Key points to

Referential Integrity
→ keep references valid

INSERT INTO
→ add actual rows

SELECT
→ retrieve rows

JOIN
→ combine related data from multiple tables
```

The most important lesson today was understanding that relational SQL is not only about writing `SELECT` queries.

The database first has a structure and rules:

```text
Schema
↓
Keys
↓
Relationships
↓
Data
↓
Queries
```

This foundation will make JOINs much easier to understand when I continue.
