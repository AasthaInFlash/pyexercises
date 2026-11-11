"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:   A single integer N provided by the user via standard input.
# 2. Process:  - The input is parsed to an integer.
   - The value of N is validated against boundary conditions (<= 0 or > upper limit).
   - If valid, a loop iterates through each integer from 1 up to N (inclusive).
   - For each value, the modulo operator (i % 2) evaluates whether the number is
     even (remainder 0) or odd (remainder 1).
# 3. Out:  - A line-by-line classification for each integer from 1 to N stating whether it
     is "odd" or "even".
   - Or, an explanatory message/prompt if the input falls outside the supported range.
# 4. What happens on 0, on a negative number, on a very large number: - On 0:
     Decision: Display a clear message stating that counting starts at 1, so no range
     exists from 1 to 0. Do not run the loop.
     Reasoning: The prompt specifies "from 1 to N". Iterating backwards or printing nothing
     silently creates ambiguous behavior for the user.
   - On a negative number (e.g., -4):
     Decision: Display an error message indicating that N must be a positive integer (>= 1).
     Reasoning: "From 1 to N" implies an ascending positive interval. Negative endpoints
     break this specification unless negative step counting is explicitly requested.
   - On a very large number (e.g., 5000):
     Decision: Set an explicit safeguard threshold (e.g., limit N to 100). If N > 100,
     reject the input with a message: "Number too large (max 100) to prevent terminal flooding."
     Reasoning: Printing 5,000 lines floods the terminal buffer, offers poor readability,
     and provides no instructional benefit over a smaller sequence.


# Your code below

MAX_ALLOWED = 100

user_input = input("Enter an integer N: ")
n = int(user_input)

if n < 0:
    print("Range error: N must be a positive integer (>= 1).")
elif n == 0:
    print("Range error: Counting starts at 1, so N must be at least 1.")
elif n > MAX_ALLOWED:
    print(f"Threshold exceeded: Please enter a number <= {MAX_ALLOWED} to prevent flooding.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")