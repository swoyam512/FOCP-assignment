# Week 2  

## Overview
This session built on Week 1 by exploring how Python handles data. Topics included variables, data types, built-in functions, strings, indexing and slicing, and lists. These concepts are key for working efficiently with Python.

---

## Variables
Variables store information that can be used later in a program. Each variable has a name chosen by the programmer.

*Rules for naming variables:*
- Must start with a letter or underscore  
- Can include letters, numbers, and underscores  
- Case-sensitive (age ≠ Age)  
- Should clearly describe the value  

Use = to assign a value to a variable. A variable must have a value before it is used.

---

## Assignment and Shortcuts
- Standard assignment evaluates the right side first.  
- Python allows *augmented assignments* like +=, -=, *=, /= to update a variable in a shorter way.

---

## Data Types
Every value in Python has a type, which affects how it behaves.  

Common types:  
- int – whole numbers  
- float – decimal numbers  
- bool – True or False  
- str – text  

Python is *dynamically typed*, so the type depends on the current value. Use type() to check a variable's type.  

Examples of type behavior:  
- + adds numbers or joins strings  
- * repeats strings

---

## Built-in Functions
Python provides ready-to-use functions:

- print() – display output  
- len() – length of string or list  
- type() – data type  
- input() – get user input  

Functions may return values and can be used inside other functions.

---

## User Input and Conversion
input() always returns a string. To perform calculations, convert input to numbers with int() or float().

---

## Strings and Quotes
Strings can be written with:  
- 'single quotes'  
- "double quotes"  
- """triple quotes"""  

*Escape characters* allow special symbols:  
- \n – newline  
- \t – tab  
- \\ – backslash  
- \' or \" – quotes  

Triple quotes support multi-line text and quotes without escapes.

---

## Indexing and Slicing
Strings are sequences of characters.

*Indexing:*  
- Zero-based  
- Access single characters  
- Negative numbers start from the end  

*Slicing:*  
- Get a substring: [start:end]  
- Start is included, end is excluded  
- Can omit indices or use negatives  
- Out-of-range slices are safe

---

## Lists
Lists are ordered collections in [ ] brackets.

- Can store multiple elements of any type  
- Can contain duplicates  
- Support indexing, slicing, concatenation (+), and repetition (*)

---

## Mutability
- *Strings* are immutable – cannot be changed  
- *Lists* are mutable – contents can be modified  

Modify lists with indexing, slicing, append(), or +=. Concatenation creates a new list instead.

---

## Key Terms
- Assignment  
- Data type  
- Argument  
- Indexing  
- Slicing  
- Mutable / Immutable  

---

