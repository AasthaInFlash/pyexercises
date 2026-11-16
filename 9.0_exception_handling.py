"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A raw text string from user input representing a divisor.
# 2. Process: Convert the string to a float and divide 100.0 by it inside a loop
#    with separate exception handlers, up to a fixed attempt limit.
# 3. Out: The division result on success, or a specific error message on failure
#    without crashing.
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: Input is non-numeric (e.g., "abc" or an empty line "").
#    - ZeroDivisionError: Input is 0, which cannot be used as a divisor.
#    - They do NOT deserve the same message because the user needs distinct guidance
#      (entering digits vs. entering a non-zero number).
#    Why catching each failure separately is better than catching all errors at once:
#    A blanket `except Exception:` hides real programming bugs (like typos/NameErrors),
#    forces a vague generic error message, and can accidentally trap interrupts.
#    Separate `except` blocks give accurate user feedback and keep real bugs visible.


# Your code below

NUMERATOR = 100.0
MAX_ATTEMPTS = 5  # TODO: Set how many attempts you allow before giving up
attempts = 0

while attempts < MAX_ATTEMPTS:
    attempts += 1
    raw_input = input(f"[Attempt {attempts}/{MAX_ATTEMPTS}] Enter a number to divide {NUMERATOR} by: ")

    try:
        divisor = float(raw_input)
        result = NUMERATOR / divisor
    except ValueError:
        print("Invalid input: that is not a number. Please type digits (e.g., 4 or 2.5).")
    except ZeroDivisionError:
        print("Math error: cannot divide by zero. Please enter a non-zero number.")
    else:
        print(f"Success: {NUMERATOR} / {divisor} = {result}")
        break
else:
    print(f"Maximum attempts ({MAX_ATTEMPTS}) reached. Exiting safely.")

# CHECK IT YOURSELF — Four runs, four behaviours:
# 1. Normal number ("4"):  Converted to float 4.0, divided 100.0 / 4.0 = 25.0, printed the result, and exited cleanly.
# 2. Zero ("0"):           Converted to float 0.0, caught ZeroDivisionError, printed the math error message, and kept running.
# 3. Word ("abc"):         Failed float conversion, caught ValueError, printed the invalid input message, and kept running.
# 4. Empty line (""):      Failed float conversion, caught ValueError, printed the invalid input message, and kept running.