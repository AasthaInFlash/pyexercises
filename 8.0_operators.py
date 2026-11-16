"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. What goes in?
#    Two hardcoded values assigned to variables: an integer (0) and an empty string ("").
#
# 2. What happens to it?
#    The program compares the two values using comparison operators (==, !=, is, is not, <, <=, >, >=),
#    checks their truthiness, and combines those results using logical operators (and, or, not).
#    It also catches TypeErrors when Python refuses to order two incompatible types.

# 3. What comes out?
#    A formatted text table printed to the console listing each operator expression alongside its
#    resulting value, boolean (True/False), or TypeError message.
#
# 4. Which two values did you pick, and which comparison result surprised you?
#    I picked 0 and "". It surprised me that both values are considered "falsy" (not a and not b are both True),
#    yet a == b evaluates to False—and attempting 0 < "" crashes with a TypeError instead of returning False.

# Your code below

a = 0
b = ""


def safe_eval(expr_str):
    try:
        return repr(eval(expr_str))
    except TypeError as e:
        return f"TypeError ({e})"


expressions = [
    # Equality & Identity
    "a == b",
    "a != b",
    "a is b",
    "a is not b",
    # Ordering
    "a < b",
    "a <= b",
    "a > b",
    "a >= b",
    # Truthiness & Logical Combinations
    "bool(a)",
    "bool(b)",
    "not a",
    "not b",
    "a and b",
    "a or b",
    "(a == b) and (not a)",
    "(a == b) or (not a)",
    "(a != b) and (not b)",
    "not (a == b)",
]

print(f"Comparing a = {repr(a)} ({type(a).__name__}) and b = {repr(b)} ({type(b).__name__})\n")
print(f"{'Expression':<25} | {'Result'}")
print("-" * 60)

for expr in expressions:
    result = safe_eval(expr)
    print(f"{expr:<25} | {result}")