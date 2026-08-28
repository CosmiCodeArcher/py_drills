base_fee = 500
distance_km = 12
rate_per_km = 75
weight_kg = 8
weight_surcharge_rate = 0.15
is_express = True

distance_charge = distance_km * rate_per_km
subtotal = base_fee + distance_charge

if weight_kg > 5:
    weight_surcharge = subtotal * weight_surcharge_rate
else:
    weight_surcharge = 0

after_surcharge = subtotal + weight_surcharge

if is_express:
    after_express = after_surcharge * 2
else:
    after_express = after_surcharge

final_total = round(after_express, 2)

one_liner_total = round(((base_fee + (distance_km * rate_per_km)) + ((base_fee + (distance_km * rate_per_km)) * weight_surcharge_rate if weight_kg > 5 else 0)) * (2 if is_express else 1), 2)

print(one_liner_total == final_total)