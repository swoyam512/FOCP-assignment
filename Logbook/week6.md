# Week 6  


---

## Working with List Methods
- Lists are *mutable sequences* that support indexing, slicing, concatenation, and iteration.  

*Common ways to modify lists:*  
- append(value) – add a single item at the end  
- extend(iterable) – add multiple items from another sequence  
- insert(index, value) – place a value at a specific position  
- remove(value) – delete the first matching value (error if not found)  
- pop([index]) – remove and return last element (or element at index)  
- clear() – remove all elements  
- sort([key=func, reverse=bool]) – sort items in place, optional key or reverse  
- reverse() – reverse the list order  

*Accessing list information:*  
- index(value, [start, end]) – find position of value  
- count(value) – count occurrences of value  
- copy() – create a shallow copy of the list  

- Use del to remove elements by index, slice, or delete the entire list variable.

---

## List Comprehensions
- A concise way to create lists in a single line.  
- Syntax example:  
```python
squares = [x**2 for x in range(10)]