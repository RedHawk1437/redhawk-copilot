# Learning Journal

---

## Session 1

Topics

- Git
- GitHub
- Repository
- Commit
- Push

Lessons

I learned how professional developers manage projects using Git.

---

## Session 2

Topics

- Project Structure
- Modules
- Python Files

Lessons

A well-structured project is easier to maintain and extend.

---

## Session 3

Topics

- XML
- ElementTree
- Root Element
- find()
- findall()
- get()

Lessons

I learned how XML stores structured scan data and how Python accesses it.

---

## Session 4

Topics

- XML Navigation
- Host Information
- Attributes
- Variables
- Debugging

Lessons

I learned how to extract host information from an Nmap XML file and debug Python errors.

I also learned the difference between elements and attributes.

Understanding the logic behind the code is more important than simply making the program work.

## Lesson: XML Lists and Loops

Today I learned that XML trees can contain multiple child elements with the same name.

Using find() returns only the first matching child.

Using findall() returns a Python list containing every matching child.

A Python for loop is then used to process each XML element individually.

This was my first successful experience parsing a real-world Nmap XML report instead of a simplified learning example.

# Learning Journal

---

## Session: Day 7

### Topics Learned

- Parsing nested XML elements.
- Understanding the relationship between `<port>` and `<service>`.
- Extracting XML attributes using `get()`.
- Processing multiple XML elements using `findall()` and `for` loops.
- Using conditional statements (`if`) to filter parsed data.
- Difference between assignment (`=`) and comparison (`==`).
- Difference between C/C++ logical operators (`&&`) and Python logical operators (`and`, `or`).
- Why each comparison must be written explicitly in Python.

### Key Takeaways

- Every `<port>` has its own `<service>` element.
- XML should always be navigated according to its tree structure.
- Good variable naming improves code readability.
- Service information is more valuable than port numbers for security analysis.
- Python executes code from top to bottom, so variables must exist before they are used.

### Confidence Level

XML Parsing        ██████████ 100%

Python Loops       █████████░ 90%

Conditional Logic  ███████░░░ 70%

Service Enumeration ██████████ 100%

Overall Python Understanding ████████░░ 80%

# Learning Journal

## Topic
Interactive XML Filtering

### Concepts Practiced

- User Input
- String Normalization
- Boolean Variables
- Integer Counters
- Conditional Statements
- XML Filtering
- Service Enumeration

### Key Lesson

A boolean variable answers:

"Was something found?"

An integer counter answers:

"How many were found?"

These two variables solve different problems and should not replace each other.

### Personal Reflection

Today I successfully implemented my first interactive search feature using Python and XML. I can now filter scan results instead of printing every available service.

# Learning Journal

## Date
2026-06-29

## What I Learned

Today I learned several important software engineering concepts.

- Functions should perform only one responsibility.
- A function should receive only the data it needs.
- Parameters should not be overwritten inside the function.
- Helper functions should generally be defined outside `main()` so they can be reused.
- The placement of a function call matters as much as the function itself.
- Separating presentation logic from data extraction improves readability.

## Personal Reflection

I can now clearly see how breaking a large program into smaller functions makes the code easier to understand and maintain. This approach feels much more professional than writing everything inside one large `main()` function.

# Learning Journal

**Date:** 2026-06-30

## What I Learned Today

Today I learned that software engineering is not only about writing working code.

It is also about separating responsibilities into small reusable functions.

I created a new function named:

```python
get_target_service()
```

which performs only one job:

- receive user input
- normalize it
- return the cleaned value

I also learned that a function should receive only the data it actually needs.

Instead of passing many individual variables, it is often better to pass the original data structure and let the function perform its own processing.

For the next refactoring step, I designed:

```python
def port_analyzer(all_ports, target_service):
```

This helped me understand that software architecture starts with deciding what responsibility belongs inside each function.

# Learning Journal

## What I Learned Today

Today I learned several important software engineering concepts.

### Function Ownership

A function should create and manage its own internal variables whenever possible.

### Multiple Return Values

Python functions can return multiple values.

Example:

```python
return target_service_found, target_service_count
```

These values can be received like this:

```python
target_service_found, target_service_count = port_analyzer(
    all_ports,
    target_service
)
```

### Gradual Refactoring

Instead of changing the entire program at once, it is better to refactor one responsibility at a time.

### Clean Architecture

A function should have only one primary responsibility.

This principle makes programs easier to read, debug, and extend.