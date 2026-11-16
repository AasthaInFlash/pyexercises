"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers (e.g., daily temperatures or scores from Exercise 4.0).
# 2. Process: The function checks if the list is empty; if not, it adds all the numbers
#    together and divides the total by how many items are in the list.
# 3. Out: A single float representing the arithmetic mean (average), or 0.0 if the list is empty.
# 4. My function name, and why return rather than print: The function is called `calculate_average`. The name clearly tells anyone reading
# the code what the function computes without needing to look inside it.
# Why `return` matters over `print`: `print()` only displays text to a human on the screen—the program itself forgets the answer immediately. `return` hands the actual
# data back to the program so it can be stored in a variable, used in further math, saved to a file, or passed into another function.


# Your code below

# 1. Defining the function
def calculate_average(numbers: list[float]) -> float:
    """Computes the arithmetic mean of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# 2. Calling it three times and printing the returned results
week_one_temps = [18.5, 20.0, 21.2, 19.8, 22.1, 23.0, 21.5]
avg_week_one = calculate_average(week_one_temps)
print(f"Week 1 average temperature: {avg_week_one:.2f}°C")

week_two_temps = [12.0, 14.5, 11.2, 13.8]
avg_week_two = calculate_average(week_two_temps)
print(f"Week 2 average temperature: {avg_week_two:.2f}°C")

single_reading = [25.4]
avg_single = calculate_average(single_reading)
print(f"Single reading average: {avg_single:.2f}°C")

# 3. Testing the empty list
empty_list = []
avg_empty = calculate_average(empty_list)
print(f"Empty list result: {avg_empty}")