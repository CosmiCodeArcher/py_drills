values = [42, 99.5, "five thousand", True, None]

immutables = 0
numerics = 0

for value in values:
    immutables += 1
    if type(value).__name__ in ["int", "float"]:
        numerics += 1
    print(f"{value} -> {type(value).__name__}")

print(f"Numeric values: {numerics}, Non-numeric: {len(values)-numerics}")

tracked = values[0]
print(type(tracked).__name__)
tracked = values[2]
print(type(tracked).__name__)
print(f"Values list at the index of zero (42) is still {values[0]}")