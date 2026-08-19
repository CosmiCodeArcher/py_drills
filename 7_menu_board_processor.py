menu = [
    {"name": "Mocha", "price": 5.00, "temp": "Hot"},
    {"name": "Iced Latte", "price": 4.50, "temp": "Cold"},
    {"name": "Espresso", "price": 3.50, "temp": "Hot"},
    {"name": "Cold Brew", "price": 4.00, "temp": "Cold"},
]

discounted_menu = list(map(lambda d: {**d, "price": d["price"] * 0.9}, menu))

cold_drinks = list(filter(lambda c: c["temp"] == "Cold", menu))

cheapest_first = sorted(menu, key=lambda s: s["price"])

cold_drinks_comprehension = [co for co in menu if co["temp"] == "Cold"]

print(discounted_menu)
print(cold_drinks)
print(cheapest_first)
print(cold_drinks_comprehension)