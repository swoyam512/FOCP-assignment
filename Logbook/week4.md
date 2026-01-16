# Week 4  


## Overview
This lab introduced *functions* in Python, which help organize code and allow reuse of logic. Topics included importing functions from modules, creating custom functions, handling different types of arguments, and using lambda expressions for simple operations.

---

## Using Built-in and Module Functions
Python comes with many *built-in functions* like print(), input(), and range(). Additional functions are grouped into *modules*, which must be imported before use.

Ways to import modules:  
- import module_name – brings in the whole module  
- from module_name import function – brings in a specific function  
- from module_name import * – imports everything (use carefully)  

Example: The math module provides functions such as sqrt() and log2(), along with constants like pi.

---

## Creating Functions
Functions are defined using def:

- Give the function a name  
- List any parameters  
- Write an indented block of code  

Functions allow you to write code once and call it multiple times. Parameters are treated as *local variables*, accessible only inside the function.

---

## Docstrings
- Docstrings are triple-quoted strings at the start of a function.  
- They explain what the function does and how it works.  
- Can be viewed using help().  
- Documenting functions improves code clarity and maintainability.

---

## Returning Values
- Use return to send a value from a function back to the caller.  
- Once return runs, the function ends.  
- If no return is specified, the function returns None.  
- Returned values can be saved in variables or used in calculations.

---

## Default Parameter Values
- You can give parameters *default values* when defining a function.  
- Parameters with defaults should come after required ones.  
- If an argument is skipped, the default is used.  

This makes functions more flexible for common use cases.

---

## Keyword Arguments
- You can call functions using *parameter names* (keyword arguments).  
- The order of keyword arguments doesn’t matter.  
- Positional arguments must come before keyword arguments.  

Keyword arguments make function calls easier to read, especially for functions with many parameters.

---

## Variable-Length Arguments
- *args allows a function to accept any number of positional arguments.  
- These arguments are stored in a tuple.  
- Useful when you don’t know how many inputs will be provided.  
- Must appear at the end of the parameter list.

---

## Lambda Functions
- *Lambda* creates small, anonymous functions in a single line.  

*Syntax:*
```python
lambda parameters : expression