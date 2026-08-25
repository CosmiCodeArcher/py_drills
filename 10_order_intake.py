import sys

print("Drink name: ", end="", file=sys.stderr)
drink_name = input()
print("Quantity: ", end="", file=sys.stderr)
drink_quantity = input()
print("Unit price: ", end="", file=sys.stderr)
drink_price = input()

try:
    drink_quantity = int(drink_quantity)
    drink_price = float(drink_price)
except ValueError:
    print("Invalid input (use numbers for quantity and price)", file=sys.stderr)
    sys.exit(1)

print(f"{drink_quantity}x {drink_name} - ${drink_price:.2f}")