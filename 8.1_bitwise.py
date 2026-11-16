"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
#   1. What goes in?
#      Individual single-bit integer flags representing specific permissions (1, 2, 4, 8).
#   2. What happens to it?
#      Bitwise OR (|) combines flags, bitwise AND (&) tests if a bit is set,
#      and AND-NOT (&= ~) clears a specific bit.
#   3. What comes out?
#      Step-by-step binary strings showing active/inactive bits (e.g., 0011 -> 0111 -> 0101)
#      and a True/False test result.
#   4. What are your permissions about? Not files: invent a set from your own field,
#      such as who may view, edit and publish a campaign.
#      E-commerce staff roles:
#        - 0001 (1): View Orders
#        - 0010 (2): Issue Refunds
#        - 0100 (4): Edit Inventory
#        - 1000 (8): Change Pricing

# Your code below

# Define permissions as single-bit flags (powers of 2)
VIEW_ORDERS    = 1 << 0  # 0b0001 (1)
ISSUE_REFUNDS  = 1 << 1  # 0b0010 (2)
EDIT_INVENTORY = 1 << 2  # 0b0100 (4)
CHANGE_PRICING = 1 << 3  # 0b1000 (8)

# 1. Combine two permissions (View Orders + Issue Refunds)
staff_perms = VIEW_ORDERS | ISSUE_REFUNDS
print(f"Combined two permissions: {staff_perms:04b}")  # 0011

# 2. Test whether a third permission (Edit Inventory) is present
has_edit = bool(staff_perms & EDIT_INVENTORY)
print(f"Has Edit Inventory?       {has_edit}")          # False

# 3. Add the third permission (Edit Inventory)
staff_perms |= EDIT_INVENTORY
print(f"After adding third:       {staff_perms:04b}")  # 0111

# 4. Remove one permission (Issue Refunds)
staff_perms &= ~ISSUE_REFUNDS
print(f"After removing one:       {staff_perms:04b}")  # 0101