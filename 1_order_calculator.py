item_price = "3.50" # Simulates two "user inputs" as strings (just hardcode them for now): item_price = "3.50" and quantity_input = "4".
quantity_input = "4"

item_price = float(item_price) # Converts both to the correct numeric types.
quantity_input = int(quantity_input)

sub_total = item_price * quantity_input # Calculates the subtotal.

if sub_total > 10: # Applies a 10% discount only if the subtotal is greater than 10.
    discounted_total = sub_total * 0.9
    print(f"Total: ${discounted_total:.2f} (discount applied)") # Prints a final message like: "Total: $12.60 (discount applied)" or "Total: $8.00" if no discount applied — using str() where needed to build the message.
else:
    print(f"Total: ${sub_total:.2f}")