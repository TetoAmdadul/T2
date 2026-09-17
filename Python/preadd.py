with open("README.md", "r") as file:
     old = file.read()

new = r"""# Day 6 — Python File Handling

## 1. What Did I Learn Today?

Today I learned the fundamentals of **File Handling in Python**.

### What is File Handling?

File handling means using Python to **read data from files, write data to files, and update existing files**.

This connects later to:

```text
TXT files
↓
CSV files
↓
Data cleaning
↓
pandas
↓
SQL / databases
↓
Data analysis
```

### Opening a File

General syntax:

```python
with open("filename.txt", "mode") as file:
    statement
```

Using `with open(...)` allows Python to open the file, work with it, and close it automatically when the block is finished.

---

### File Modes

#### Read Mode — `"r"`

Used to read an existing file.

```python
with open("customer_report.txt", "r") as file:
    content = file.read()
```

```text
"r" → read
```

---

#### Write Mode — `"w"`

Used to write data to a file.

```python
with open("customer_report.txt", "w") as file:
    file.write("Customer Order Report\n")
```

Important:

```text
"w"
→ writes data
→ replaces existing file content
```

---

#### Append Mode — `"a"`

Used to add new content without deleting existing content.

```python
with open("customer_report.txt", "a") as file:
    file.write("Amina 2320\n")
```

```text
"a"
→ keeps old content
→ adds new content at the end
```

---

### `.read()`

`.read()` reads the complete file content.

```python
with open("customer_report.txt", "r") as file:
    content = file.read()

print(content)
```

---

### `.write()`

`.write()` writes text into a file.

```python
with open("customer_report.txt", "w") as file:
    file.write("Customer Order Report\n")
```

In the Python REPL, `.write()` can display the number of characters written.

Example:

```python
file.write("Customer Order Report\n")
```

returned:

```text
22
```

This means 22 characters were written to the file.

---

### Newline — `\n`

`\n` means **new line**.

```python
file.write("Customer Order Report\n")
```

Without `\n`, the next Terminal prompt may appear on the same line as the file content.

---

### Reading a File Line by Line

Instead of reading the whole file at once, I can process one line at a time.

General syntax:

```python
with open("filename.txt", "r") as file:
    for line in file:
        print(line)
```

Example:

```python
with open("customer_report.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### `.strip()`

`.strip()` removes unnecessary whitespace and newline characters from the beginning and end of a string.

General syntax:

```python
string.strip()
```

Example:

```python
print(line.strip())
```

---

### File Line Counter

I also connected file handling with the counter pattern:

```python
with open("customer_report.txt", "r") as file:
    count = 0

    for line in file:
        count = count + 1

print(count)
```

This counted how many lines were in the file.

---

### Key Programming Terms

- File handling
- File
- `open()`
- File mode
- Read mode
- Write mode
- Append mode
- `.read()`
- `.write()`
- `.strip()`
- File object
- Newline
- Line-by-line processing
- Counter
- `with` statement


## 2. What Did I Do Today?

I created and worked with text files using Python.

### Read an Existing File

I read:

```text
1200
850
2100
600
```

using:

```python
with open("file_handle_python.txt", "r") as file:
    content = file.read()

print(content)
```

---

### Created a Customer Report

I wrote:

```text
Customer Order Report
```

to:

```text
customer_report.txt
```

using:

```python
with open("customer_report.txt", "w") as file:
    file.write("Customer Order Report\n")
```

---

### Appended Customer Data

I added new data without removing the existing report:

```text
Amina 2320
Rafi 2750
```

using append mode.

The final file contained:

```text
Customer Order Report
Amina 2320
Rafi 2750
```

---

### Read the Final File in the Python REPL

```python
with open("customer_report.txt", "r") as file:
    content = file.read()

print(content)
```

Output:

```text
Customer Order Report
Amina 2320
Rafi 2750
```

---

### Read the File Line by Line

```python
with open("customer_report.txt", "r") as file:
    for line in file:
        print(line.strip())
```

Output:

```text
Customer Order Report
Amina 2320
Rafi 2750
```

---

### Counted the Number of Lines

```python
with open("customer_report.txt", "r") as file:
    count = 0

    for line in file:
        count = count + 1

print(count)
```

Output:

```text
3
```

I also used Terminal to check file contents:

```bash
cat customer_report.txt
```


## 3. Interview Questions & Answers

### What is file handling in Python?

File handling is the process of reading, writing, or updating data stored in files.

### What does `open()` do?

`open()` opens a file so Python can work with it.

### What does `"r"` mean?

`"r"` means **read mode**.

It is used to read an existing file.

### What does `"w"` mean?

`"w"` means **write mode**.

It writes data to a file and can replace existing content.

### What does `"a"` mean?

`"a"` means **append mode**.

It adds new content to the end of a file without deleting the existing content.

### Why use `with open(...)`?

It provides a clean way to work with files and automatically closes the file when the block finishes.

### What is the difference between `.read()` and `for line in file`?

`.read()` reads the whole file at once.

```python
file.read()
```

`for line in file` processes the file one line at a time.

```python
for line in file:
```

### What does `.write()` do?

`.write()` writes a string into a file.

### Why did `.write()` return `22` in the REPL?

`.write()` returns the number of characters successfully written to the file.

### What does `\n` mean?

`\n` represents a newline character.

### What does `.strip()` do?

`.strip()` removes leading and trailing whitespace, including newline characters.

### Can files be read directly in the Python REPL?

Yes.

The same file-handling syntax works in both the REPL and `.py` files.

### Why would I read a file line by line?

Line-by-line processing is useful when each line needs to be processed separately and is also useful for larger files.


## 4. Summary — Mistakes & Corrections

### Mistake: Opening a `with` block without an indented statement

I wrote:

```python
with open("customer_report.txt", "w") as file:
```

and finished the block without writing anything inside it.

This caused:

```text
IndentationError: expected an indented block
```

Correction:

```python
with open("customer_report.txt", "w") as file:
    file.write("Customer Order Report")
```

I learned that code after a line ending with `:` must contain an indented block.

---

### Issue: File output and Terminal prompt appeared on the same line

I originally wrote:

```python
file.write("Customer Order Report")
```

The file had no newline at the end.

Correction:

```python
file.write("Customer Order Report\n")
```

I learned that:

```text
\n
```

moves the following output to a new line.

---

### Mistake: Typing `exit` instead of `exit()`

In the Python REPL I typed:

```text
exit
```

Python reminded me to use:

```python
exit()
```

or:

```text
Ctrl + D
```

I used `Ctrl + D` successfully to return to the normal Terminal.

---

### Important File Mode Difference

```text
"r"
→ read existing content

"w"
→ write and replace content

"a"
→ add content without deleting old content
```

---

### Important Connection

Today I connected previous Python knowledge with file handling:

```text
File
↓
for loop
↓
one line at a time
↓
.strip()
↓
counter
↓
process real data
```

This prepares me for **CSV files, data cleaning, pandas, SQL and real business datasets**.
"""

with open("README.md", "w") as file:
     file.write(new + "\n\n" + old)
