"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: Three pieces of user input typed into the terminal: customer_name (text),
#    item_type (text), and price_eur (a positive decimal number).
# 2. Process: - Validation: Empty text inputs are rejected in a loop until the user types a valid
#      non-empty string. Price is checked to ensure it is a valid number greater than 0;
#      invalid or negative numbers prompt the user to re-enter without crashing.
#    - First-run header check: Before writing, the program checks if `craft_orders.csv`
#      already exists (and is non-empty). If not, it opens the file in write mode to
#      create the header row first.
#    - Appending: It opens the CSV in append mode (`"a"`) so each run adds a new row
#      at the bottom without overwriting existing entries.
# 3. Out, file name and columns: - File name: `craft_orders.csv`
#    - Columns: `customer_name,item_type,price_eur`
# 4. Why these columns, and what this file is for: I chose customer_name, item_type, and price_eur to track handmade craft sales.
#    Once this file has 200 rows, I can analyze which product types generate the most
#    revenue, calculate total and average order values, and identify repeat customers.


# Your code below

import csv
import os

FILENAME = "craft_orders.csv"
HEADERS = ["customer_name", "item_type", "price_eur"]


def get_non_empty_text(prompt: str) -> str:
    """Keeps asking until the user enters non-empty text without commas that break simple CSVs."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_price(prompt: str) -> float:
    """Keeps asking until the user enters a valid number greater than 0."""
    while True:
        raw = input(prompt).strip()
        try:
            price = float(raw)
            if price > 0:
                return round(price, 2)
            print("Price must be greater than 0.")
        except ValueError:
            print("Invalid number. Please enter a valid price (e.g., 25.50).")


def save_order(filename: str, row: list) -> None:
    """Creates the file with a header if missing, otherwise appends a new row."""
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(HEADERS)
        writer.writerow(row)


def main() -> None:
    print("--- New Craft Order Entry ---")
    customer = get_non_empty_text("Customer name: ")
    item = get_non_empty_text("Item ordered (e.g., Resin Frame, Nameplate): ")
    price = get_positive_price("Price in EUR: ")

    save_order(FILENAME, [customer, item, f"{price:.2f}"])
    print(f"Saved order for {customer} to {FILENAME}.")


if __name__ == "__main__":
    main()