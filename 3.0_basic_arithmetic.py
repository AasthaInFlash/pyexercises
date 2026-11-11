"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two numbers entered by the user via standard input (converted from strings
   to floating-point numbers using float() to support decimals).
# 2. Process:  The numbers are converted to numeric types, and the four standard arithmetic
   operations are applied: addition (+), subtraction (-), multiplication (*),
   and true division (/).
# 3. Out: Printed lines displaying the equation and calculated result for each of
   the four operations.
# 4. What happens when the second number is zero, and why: Decision: Display an informative message for the division operation instead
   of a numeric result ("Division by zero is undefined"), while still displaying
   the results for addition, subtraction, and multiplication.
   Defense: Addition, subtraction, and multiplication by zero are mathematically
   valid and informative (e.g., 5 * 0 = 0). Crashing the program or refusing to show
   the other valid operations would discard useful calculations.


# Your code below

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2


print("\n--- Results ---")
print(f"{num1} + {num2} = {add_result}")
print(f"{num1} - {num2} = {sub_result}")
print(f"{num1} * {num2} = {mul_result}")

if num2 == 0:
    print(f"{num1} / {num2} = Undefined (division by zero is not allowed)")
else:
    div_result = num1 / num2
    print(f"{num1} / {num2} = {div_result}")

