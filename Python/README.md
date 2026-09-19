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
