#  Python OOP Student Management System

A beginner-friendly Python project that demonstrates Object-Oriented Programming (OOP) concepts along with Python data structures such as lists, dictionaries, sets, and tuples.

---

##  Project Overview

This project simulates a simple **student management system** where you can:
- Store student information
- Add and manage grades
- Calculate averages
- Use different Python data structures
- Validate emails using regular expressions

It is designed to help beginners understand how OOP works in real-world Python applications.

---

##  Features

### Student Class
Each student has:
- Name
- Email
- Grades (list)

### Methods:
- Add grades
- Calculate average grade
- Display student information
- Convert grades to a tuple

---

##  Concepts Used

- Object-Oriented Programming (OOP)
- Classes & Objects
- Methods
- Lists
- Dictionaries
- Sets
- Tuples
- Regular Expressions (`re`)
- Error handling (`try/except`)
- Loops & conditionals

---

##  Project Structure

```
Object_Oriented_Practice.py   # Contains all class definitions and program logic
```

---

##  How It Works

1. Create student objects with name, email, and initial grades  
2. Add new grades using methods  
3. Store students in a dictionary using email as the key  
4. Perform operations like:
   - View student info
   - Calculate averages
   - Get unique grades
   - Validate emails
   - Work with tuples and lists

---

##  How to Run

### 1. Install Python
Make sure Python 3 is installed:
```bash
python --version
```

### 2. Run the program
```bash
python main.py
```

---

##  Example Output

```
Name: Alice
Email: alice@gmail.com
Grades: [85, 90, 100, 80]
Average Grade: 88.75
```

```
Unique Grades: {80, 85, 90, 100}
```

```
Grades above 90: 3
```

---

##  Email Validation

The program checks if emails follow this format:

```
name@domain.com
```

---

##  Tuple Immutability Demo

The project demonstrates that tuples cannot be changed:

```
Error: Tuples are immutable!
```

---

## 📈 Future Improvements

- Add a menu-driven CLI interface
- Save student data to a file (JSON or CSV)
- Add student deletion and editing features
- Build a GUI version using Tkinter

---

## Author

Beginner Python OOP Project for learning purposes.

---
```