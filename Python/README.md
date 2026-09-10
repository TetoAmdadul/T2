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
