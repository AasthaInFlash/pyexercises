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

# 1. In: A pre-defined list of 14 integers representing daily batch units received at a distribution warehouse across a two-week cycle: [3, 5, 7, 9, 11, 13, 15, 17, 1, 2, 4, 6, 8, 10].
# 2. Process: - Access specific individual items by index (e.g., indices 0 and 1). Create a sorted copy of the list using sorted() without mutating the original. Remove the last recorded day using .pop() to simulate dropping an incomplete shift. Compute aggregate statistics: total units (sum) and average units per shift (sum / len).
# 3. Out: Console outputs displaying: The complete initial list. Chosen individual items by position. The list in sorted ascending order. The popped item and the updated list state. Computed metrics: total units processed and the average units per shift.
# 4. What my list is about, and what I computed from it: - Domain context: Daily batch intake numbers for warehouse inventory control. What was computed: The total intake (sum = 91 units across 13 recorded batches)  and the average daily batch size (7.0 units). Why it is interesting: It establishes baseline inbound volume, helping warehouse   managers forecast staffing requirements and benchmark daily worker capacity.


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