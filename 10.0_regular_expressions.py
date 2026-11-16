"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. What goes in?
#    Three text strings typed by the user via input(): a campaign code, a launch date,
#    and a contact email.
#
# 2. What happens to it?
#    Each string has outer whitespace stripped and is checked against a regular expression
#    using re.fullmatch(). Only if all three pass validation are they saved together.
#
# 3. What comes out?
#    Per-field pass/fail feedback, and either a confirmation message with the saved record
#    or a rejection message stating nothing was saved.
#
# 4. What are your three fields, and what makes a value acceptable for each?
#    - Field 1 (Campaign Code): Must start with uppercase "CMP-" followed by exactly
#      4 digits (e.g., "CMP-1042"). Reject lowercase prefixes, spaces, or fewer/more digits.
#    - Field 2 (Launch Date): Must follow the YYYY-MM-DD shape (4 digits, hyphen, 2 digits,
#      hyphen, 2 digits). Reject slashes or 2-digit years.
#    - Field 3 (Contact Email): Must have a username (letters, numbers, ., _, -), a single "@",
#      a domain name, a literal dot, and a domain extension of at least 2 letters. Reject
#      spaces, missing "@", or single-letter extensions.

# Your code below

import re

# 1. Campaign Code: ^ and $ anchor start/end; CMP- matches literal text; \d{4} requires 4 digits.
CODE_PATTERN = r"^CMP-\d{4}$"

# 2. Launch Date: ^ and $ anchor start/end; \d{4}, \d{2}, \d{2} match digit groups separated by hyphens.
DATE_PATTERN = r"^\d{4}-\d{2}-\d{2}$"

# 3. Contact Email: ^ and $ anchor start/end; [a-zA-Z0-9._-]+ matches 1+ username chars;
#    @ matches literal @; [a-zA-Z0-9.-]+ matches domain; \. matches a literal dot;
#    [a-zA-Z]{2,} requires 2 or more letters for the ending extension.
EMAIL_PATTERN = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def validate_and_save():
    code = input("Enter Campaign Code (e.g., CMP-1042): ").strip()
    date = input("Enter Launch Date (YYYY-MM-DD): ").strip()
    email = input("Enter Contact Email: ").strip()

    code_ok = bool(re.fullmatch(CODE_PATTERN, code))
    date_ok = bool(re.fullmatch(DATE_PATTERN, date))
    email_ok = bool(re.fullmatch(EMAIL_PATTERN, email))

    if not code_ok:
        print("Invalid Campaign Code: must be 'CMP-' followed by 4 digits.")
    if not date_ok:
        print("Invalid Launch Date: must match YYYY-MM-DD.")
    if not email_ok:
        print("Invalid Contact Email: must be a standard name@domain.ext address.")

    if code_ok and date_ok and email_ok:
        saved_record = {
            "campaign_code": code,
            "launch_date": date,
            "contact_email": email,
        }
        print("All three fields valid! Saved:", saved_record)
    else:
        print("Validation failed. Nothing was saved.")


if __name__ == "__main__":
    validate_and_save()

# CHECK IT YOURSELF — 9 test cases (1 pass + 2 fail per field):
# Campaign Code:
#   - Pass: "CMP-2026"   -> Accepted
#   - Fail: "cmp-2026"   -> Rejected (lowercase prefix)
#   - Fail: "CMP-12"     -> Rejected (only 2 digits)
# Launch Date:
#   - Pass: "2026-11-16" -> Accepted
#   - Fail: "16/11/2026" -> Rejected (uses slashes and DD/MM/YYYY order)
#   - Fail: "26-11-16"   -> Rejected (2-digit year)
# Contact Email:
#   - Pass: "alex@studio.fr" -> Accepted
#   - Fail: "alex@studio"    -> Rejected (no dot + TLD extension)
#   - Fail: "alex studio@x.com" -> Rejected (contains a space)
# Surprises noted during testing:
#   - No unexpected failures on the 9 test cases, though re.fullmatch() checks
#     only digit shape (e.g., "2026-99-99" would pass) rather than calendar validity,
#     and .strip() silently trims leading/trailing spaces before validation.