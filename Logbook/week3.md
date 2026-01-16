# Week 3  


## Overview
In this lab, we explored *decision-making and repetition* in Python. We learned how to use Boolean expressions, logical and relational operators, if, elif, else statements, loops (while and for), membership checks, ternary operators, and loop controls like break and continue. These concepts allow Python programs to act based on conditions and repeat tasks efficiently.

---

## Boolean Expressions
Boolean expressions evaluate to True or False and control program flow.

- *Relational operators:* <, >, <=, >=, ==, !=  
- Usually involve variables rather than fixed values.  

Examples: comparing numbers, text, or list elements.  
*Tip:* Avoid comparing incompatible types. Remember, input() returns a string, so numeric input may need conversion.

---

## Logical Operators
Logical operators combine multiple conditions:

- and – True if all conditions are True  
- or – True if at least one condition is True  
- not – Reverses the Boolean value  

Parentheses help clarify evaluation order. Python also supports *chained comparisons* for concise expressions.

---

## Membership Operators
Check if a value exists in a collection (string, list, etc.):

- in – True if present  
- not in – True if absent  

Useful as an alternative to multiple relational checks.

---

## Conditional Statements (if)
if statements execute a block of code only when a condition is True.

- Indentation defines the code block  
- Conditions are typically Boolean expressions  

### elif and else
- elif – checks additional conditions  
- else – runs if no previous conditions are True  
- Only one block runs in an if-elif-else chain  

Non-Boolean values are treated as False (0, "", []) or True (non-zero numbers, non-empty sequences). Using explicit Boolean expressions improves readability.

---

## Ternary Operator
The ternary operator is a compact way to write if-else statements on one line.

*Syntax:*
```python
value_if_true if condition else value_if_false