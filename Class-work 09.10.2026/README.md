# Class-work 09.10.2026

**Topic:** Web Application Development with Python  
**Module:** Tuples, Sets, and Dictionaries

A menu-driven Python console project implementing every task in the assignment. All user-facing text and code comments are in English.

## Requirements
- Python 3.10 or newer
- No external packages

## Run
From the project folder:

```bash
python src/main.py
```

On Windows, you can also run `run.bat` or use `py src/main.py`.

## Included tasks

### Part 1
1. Count occurrences of a user-entered fruit in a tuple.
2. Display a tuple that includes repeated fruit names.
3. Replace all full-name matches of a car manufacturer. Matching is case-insensitive, but the entire name must match. The list contains Lamborghini, Ferrari, Bentley, Rolls-Royce, and Bugatti.

### Part 2
1. Manage a set of countries: add, remove, substring search, and exact membership check.
2. Find city names present in both sets (intersection).
3. Find city names present only in the first set (difference).
4. Find city names present only in the second set (reverse difference).
5. Find city names unique to either set (symmetric difference).
6. Manage country-to-capital dictionary entries: add, delete, search, and replace a capital.

For city tasks, enter city names separated by commas, for example: `Berlin, Hamburg, Munich`.

## Important Python concept
Tuples are immutable. Therefore, repeated fruits are included when the tuple is created rather than appended to an existing tuple. Sets automatically keep only unique values.
