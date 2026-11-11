"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of 5 destination strings: places = ["Kyoto", "Reykjavik", "Cusco", "Cape Town", "Banff"].
# 2. Process: Create temporary reordered copies using sorted() and slicing [::-1], avoiding mutating methods like .sort() and .reverse().
# 3. Out: Printed versions of the list in 4 new orders, followed by the unchanged original list.
# 4. My four orders, and which ones modify the original: - Order 1: Alphabetical (sorted(places)) -> Returns a new copy.
Order 2: Reverse alphabetical (sorted(places, reverse=True)) -> Returns a new copy.
Order 3: Reversed original sequence (places[::-1]) -> Returns a new slice copy.
Order 4: Sorted by word length (sorted(places, key=len)) -> Returns a new copy.
None of them modify the original list.


# Your code below

places = ["Kyoto", "Reykjavik", "Cusco", "Cape Town", "Banff"]

print("Original list:")
print(places)
print("-" * 40)

print("1. Alphabetical order:")
print(sorted(places))

print("2. Reverse alphabetical order:")
print(sorted(places, reverse=True))

print("3. Reversed original sequence:")
print(places[::-1])

print("4. Sorted by length of place name:")
print(sorted(places, key=len))

print("-" * 40)
print("Proof - Original list is unchanged:")
print(places)
