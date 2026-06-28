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