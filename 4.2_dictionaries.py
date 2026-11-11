"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A dictionary with 5 initial fields describing a product ("sku", "title", "unit_price", "stock_quantity", "is_clearance").
# 2. Process: Read a field by key, safely query a missing key using .get(), update "unit_price", remove "is_clearance" with .pop(), and iterate over all remaining items.
# 3. Out: Printed outputs showing the read value, the safe fallback for the missing key, the updated price, the removed value, and all remaining key-value pairs.
# 4. My object, my five fields, and why those: Object: An e-commerce product SKU.
- "sku": Unique identifier for warehouse lookup.
- "title": Name displayed on the storefront.
- "unit_price": Base price used for checkout.
- "stock_quantity": Available inventory count.
- "is_clearance": Flag to trigger clearance discounts.
Missing key note: product["warehouse_bin"] throws a KeyError; product.get() avoids the crash by returning a default value.


# Your code below

product = {
    "sku": "TECH-WH-1004",
    "title": "Noise-Cancelling Wireless Headphones",
    "unit_price": 149.99,
    "stock_quantity": 42,
    "is_clearance": False
}

print("Current Stock Quantity:", product["stock_quantity"])

missing_value = product.get("warehouse_bin", "Default: Unassigned")
print("Querying non-existent field 'warehouse_bin':", missing_value)

product["unit_price"] = 129.99
print("Updated Price:", product["unit_price"])

removed_status = product.pop("is_clearance")
print("Removed 'is_clearance' status:", removed_status)

print("\nFinal Product Record:")
for field, value in product.items():
    print(f"  {field}: {value}")