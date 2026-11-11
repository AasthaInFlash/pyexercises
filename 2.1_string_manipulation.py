"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:    A single string (sentence) entered by the user via standard input.
# 2. Process:  The raw input string is processed using four distinct Python string methods:
   .strip(), .upper(), .title(), and .replace().
# 3. Out: Four formatted lines printed to the console, each displaying the result of one
   specific transformation applied to the original input.
# 4. My four transformations, and when each is useful:
- strip(): Useful for cleaning user input forms to eliminate accidental leading/trailing whitespace before storing in a database.
   - upper(): Useful for case-insensitive comparisons, such as standardizing promo codes or airport codes (e.g., 'jfk' -> 'JFK').
   - title(): Useful for formatting names, book titles, or article headlines where each word must start with an uppercase letter.
   - replace(): Useful for sanitizing text or creating URL-friendly slugs by swapping characters (e.g., replacing spaces with hyphens).

# Your code below

raw_text = input("Please enter a sentence: ")

cleaned_text = raw_text.strip()
shouted_text = raw_text.upper()
title_text = raw_text.title()
slugified_text = raw_text.replace(" ", "-")

print("\n--- Transformed Results ---")
print("1. Stripped whitespace :", cleaned_text)
print("2. Uppercase           :", shouted_text)
print("3. Title case          :", title_text)
print("4. Replaced spaces (-) :", slugified_text)