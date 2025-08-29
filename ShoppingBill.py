# ShoppingBill.py

def calculate_total_with_tax(item_prices, tax_percent):
    subtotal = sum(item_prices)
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

# Input prices for 3 items
item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))
item3 = float(input("Enter price of item 3: ₹"))

# Input tax percentage
tax_percent = float(input("Enter tax percentage: "))

# Calculate totals
subtotal, tax, total = calculate_total_with_tax([item1, item2, item3], tax_percent)

# Display the results
print("\n--- Shopping Bill ---")
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax:.2f}")
print(f"Total: ₹{total:.2f}")
