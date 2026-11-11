# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-11-10 14:58, in .

**Me:** how to print in python

**Tutor:**

Printing in Python is done with the `print()` function.

```python
# This prints a single value
print("Hello, world!")

# This prints multiple values separated by a space
print("Cost:", 19.99)
```

What is the argument you pass to `print()`?

---
## 2026-11-10 15:54, in .

**Me:** how to add two numbers

**Tutor:**

Adding two numbers in Python is done with the `+` operator.

```python
def add_two_numbers(a, b):
    # TODO: return the sum of a and b
    pass
```

What is the operator that combines two values into a single sum?

---
## 2026-11-10 17:23, in .

**Me:** how to add two numbers

**Tutor:**

Concept: Adding two numbers with the `+` operator.

Pattern:
```python
def add_numbers(a, b):
    # TODO: return the sum of a and b
    pass
```

Question: What operator is used to add `a` and `b` in the function above?
How to reverse a list

---
## 2026-11-11 10:11, in .

**Me:** how to reverse a list

**Tutor:**

Reversing a list in Python.

```python
def reverse_list(items):
    # TODO: return a new list with the elements in reverse order
    pass

# Example usage
original = [10, 20, 30]
reversed_items = reverse_list(original)
print(reversed_items)  # Should print [30, 20, 10]
```

Which built-in list method reverses the order of elements in place?

---
## 2026-11-11 10:11, in .

**Me:** what is dictionary can we store numbers

**Tutor:**

Dictionaries store key-value pairs.

```python
def make_price_map():
    # TODO: create a dictionary that maps product names (strings) to prices (numbers)
    pass

# Example
prices = make_price_map()
print(prices["alpha"])  # Should print a number
```

Name the type used for dictionary keys in Python.

---
## 2026-11-11 10:12, in .

**Me:** what is the difference between while loops and for loops

**Tutor:**

Difference between while and for loops.

```python
# while loop – runs as long as a condition is True
count = 0
while count < 3:          # condition
    print("while", count)
    count += 1

# for loop – iterates over a sequence (list, string, range…)
for value in [10, 20, 30]:  # sequence
    print("for", value)
```

Which loop type should you use when you know exactly how many times you want to repeat something?

---
## 2026-11-11 10:12, in .

**Me:** what is list manipulation howto sort a list

**Tutor:**

List manipulation: sorting a list.

```python
def sort_prices(prices):
    # TODO: return a new list with the prices sorted in ascending order
    pass

# Example
original = [3.99, 1.50, 2.75]
sorted_prices = sort_prices(original)
print(sorted_prices)  # Should print [1.5, 2.75, 3.99]
```

Which built-in function returns a new sorted list without changing the original?

---
## 2026-11-11 10:13, in .

**Me:** how to check if a number is odd or even

**Tutor:**

Checking if a number is odd or even.

```python
def is_even(number):
    # TODO: return True if the number is even, False if it is odd
    pass

# Example
print(is_even(4))  # Should print True
print(is_even(7))  # Should print False
```

Which operator do you use with the modulus (%) to test divisibility by 2?

---
## 2026-11-11 10:25, in .

**Me:** how to replace any numbers or text

**Tutor:**

String replacement in Python.

```python
def clean_text(text):
    # TODO: return the text with every digit replaced by '#' and every letter by '*'
    pass

# Example
dirty = "a1b2c3"
clean = clean_text(dirty)
print(clean)  # Should print "***###"
```

Which string method replaces all occurrences of a substring?

---
## 2026-11-11 10:44, in .

**Me:** how to check if a number is odd

**Tutor:**

Checking if a number is odd.

```python
def is_odd(number):
    # TODO: return True if the number is odd, False otherwise
    pass

# Example
print(is_odd(5))  # Should print True
print(is_odd(4))  # Should print False
```

Which operator combined with 2 gives the remainder when dividing the number?

---
## 2026-11-11 10:45, in .

**Me:** what is the equals to sign

**Tutor:**

The equals sign in Python.

```python
# Assignment
x = 10

# Comparison
y = 20
print(x == y)  # prints False
```

What keyword tests equality in an if-statement?

---
## 2026-11-11 10:56, in .

**Me:** what values can we add to the dictionary

**Tutor:**

Dictionary values can be any Python object: numbers, strings, lists, other dictionaries, booleans, None, etc.

```python
def build_sample_dict():
    # TODO: return a dictionary whose values are one number, one string, one list, and one boolean
    pass

# Example
sample = build_sample_dict()
print(sample["price"])   # prints a number
print(sample["tags"])    # prints a list
```

Name the type used for dictionary keys in Python.

---
## 2026-11-11 10:56, in .

**Me:** how to reverse a list

**Tutor:**

Reversing a list.

```python
def reverse_list(items):
    # TODO: return a new list with the elements in reverse order
    pass

# Example
original = ["alpha", "beta", "gamma"]
reversed_items = reverse_list(original)
print(reversed_items)  # Should print ['gamma', 'beta', 'alpha']
```

Which built-in function returns an iterator that yields items in reverse order?
