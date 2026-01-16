# Week 7  


---

## Sets
- Sets are *unordered collections* of unique elements.  
- The set itself is mutable, but its items must be immutable (e.g., no lists).  
- Cannot use indexing or slicing because order is not guaranteed.  
- Excellent for *fast membership checks* using in or not in.  
- Create sets with curly braces {} or set():

```python
vowels = {"a", "e", "i", "o", "u"}
names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])