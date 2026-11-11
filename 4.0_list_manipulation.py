"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. What my list is about, and what I computed from it:


# Your code below
number_1 = 2
number_2 = 4
number_3 = 6
number_4 = 8
number_5 = 10

print("The first number is : ", number_1)
print("The second number is : ", number_2)
print("The third number is : ", number_3)
print("The third number is : ", number_4)
print("The third number is : ", number_5)

numbers = [3,5,7,9,11,13,15,17,1,2,4,6,8,10]
print("The whole list is : ", numbers)
print("The second item of the list is : ", numbers[1])
print("The first item of the list is : ", numbers[0])

sorted_numbers = sorted(numbers)
print("The sorted list is : ", sorted_numbers)

removed_number = numbers.pop()
print("The removed item is : ", removed_number)
print("The list after removing the last item is : ", numbers)
print("The sorted list after removing the last item is : ", sorted_numbers)