# Week 5  


## Overview
This lab covered *Python scripts and modules*. We learned how programs are saved in files, executed from the operating system, and structured for reuse. Topics included interactive vs. script mode, command-line arguments, importing modules, and how Python manages external code. These skills help organize larger programs effectively.

---

## Python Scripts
A Python script is a program saved in a .py file and run from the terminal or command prompt.  

- Unlike interactive mode, scripts do not display results automatically; use print() for output.  
- Scripts can be created in any text editor, though IDEs provide extra features like debugging and syntax highlighting.

---

## Running Scripts and Command-Line Arguments
Scripts are executed using the Python interpreter from the terminal.  

- Extra values can be passed using *command-line arguments*.  
- Access these arguments via the sys module using sys.argv, a list of strings:  
  - sys.argv[0] – script name  
  - sys.argv[1:] – user-provided arguments  

Command-line arguments let programs behave differently without changing the code.

---

## Using the sys Module
The sys module gives access to system-specific information.  

- Importing sys allows scripts to read command-line arguments and interact with the environment.  
- Check len(sys.argv) to ensure required arguments are provided and handle missing input safely.

---

## Importing Modules and Aliases
Python lets you import entire modules or specific functions/classes.  

- Modules can be given *aliases* for shorter names or to avoid conflicts.  
- Import only what you need for clarity and efficiency.  
- Avoid from module import * as it can cause naming conflicts.

---

## Symbol Tables
Python tracks names and their associated objects using *symbol tables*.  

- Each module has its own symbol table to prevent conflicts.  
- Use dir(module) to list all names in a module for exploration or debugging.

---

## Module Search Path
Python searches directories in the list defined by sys.path when importing modules.  

- Knowing this path helps when working with custom modules or troubleshooting import errors.

---

## The __name__ Variable
- Python automatically assigns __name__ to each module.  
- If a file is run as a script, __name__ = "__main__"  
- If imported, __name__ equals the module’s name  

This allows code to run only when intended.

---

## Conclusion
This lab helped understand how Python programs are structured and executed. By creating scripts, using command-line arguments, importing modules, and managing namespaces, we learned key skills for building *reusable, organized, and scalable* Python programs, preparing us for more advanced coding tasks.