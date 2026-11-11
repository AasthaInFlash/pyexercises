"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: User console text inputs prompted up to 4 times (e.g., "yes", "no", or invalid strings).
# 2. Process: Log each raw input, normalize it with .strip().lower(), validate against accepted values ("yes"/"y" or "no"/"n"), track attempt count, and terminate early on valid input or break after reaching the safety limit.
# 3. Out: Immediate feedback per attempt plus a final session summary showing final status, total attempts used, and the input history list.
# 4. My stop condition, my attempt limit, my summary: - Stop condition: User enters "yes"/"y" or "no"/"n" (case- and space-insensitive).
- Attempt limit: 4 attempts max; defaults to "TIMED_OUT" if exceeded.
- Summary contains: Final outcome status, attempt count vs. max allowed, and logged entries.


# Your code below

MAX_ATTEMPTS = 4
attempts = 0
responses_log = []
status = "timed_out"

while attempts < MAX_ATTEMPTS:
    user_input = input(f"[Attempt {attempts + 1}/{MAX_ATTEMPTS}] Do you want to proceed? (yes/no): ")
    responses_log.append(user_input)
    attempts += 1
    
    cleaned_input = user_input.strip().lower()
    
    if cleaned_input in ("yes", "y"):
        status = "confirmed"
        print("-> Action confirmed successfully.")
        break
    elif cleaned_input in ("no", "n"):
        status = "cancelled"
        print("-> Action cancelled by user.")
        break
    else:
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"-> Invalid input '{user_input.strip()}'. {remaining} attempt(s) remaining.")
        else:
            print(f"-> Invalid input '{user_input.strip()}'. Maximum attempts reached.")

print("\n" + "=" * 40)
print("SESSION SUMMARY")
print("=" * 40)
print(f"Final Status:     {status.upper()}")
print(f"Attempts Used:    {attempts} of {MAX_ATTEMPTS}")
print(f"Input History:    {responses_log}")
print("=" * 40)