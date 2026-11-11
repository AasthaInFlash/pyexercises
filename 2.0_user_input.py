"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: item_name: A string entered by the user representing the inventory item/part name.
stock_input: A string of digits entered by the user representing current units in the warehouse.
# 2. Process: - Prompt the user and capture both values as strings using input(). Convert stock_input from a string into an integer using int() so arithmetic is possible. Add 1 to current_stock to calculate projected_stock after a test unit check-in. Construct a final formatted status message using an f-string combining the name, current stock, and projected stock.
# 3. Out: A printed status message summarizing the reorder status and updated inventory level.
# 4. My two fields, and what I would do with them: Field 1: Item / Part Name (e.g., "Brake Caliper Assembly")
Field 2: Current Stock Level (e.g., 14)
Purpose (Supply Chain / Warehouse Ops): On a daily inventory log form, the operations team records an item identifier alongside physical stock. The system calculates upcoming
inventory adjustments (stock + 1 incoming sample batch) and generates a restocking summary.


# Your code below
item_name = input("Enter the inventory item/part name: ")
stock_input = input("Enter current units in warehouse: ")



current_stock = int(stock_input)
projected_stock = current_stock + 1


print(f"Inventory update logged: Item '{item_name}' currently has {current_stock} units, "
    f"and will reach {projected_stock} units once the incoming test unit is checked in."
)
