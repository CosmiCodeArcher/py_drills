rules = [
    {"name": "oversize",     "field": "weight_kg", "op": ">",  "value": 30,    "action": "reject: exceeds 30kg"},
    {"name": "remote",       "field": "zone",      "op": "==", "value": "remote", "action": "surcharge: 2500"},
    {"name": "fragile",      "field": "fragile",   "op": "==", "value": True,  "action": "surcharge: 1500"},
    {"name": "bulk",         "field": "weight_kg", "op": ">",  "value": 10,    "action": "surcharge: 800"},
    {"name": "express",      "field": "service",   "op": "==", "value": "express", "action": "surcharge: 3000"},
]

parcels = [
    {"id": "P1", "weight_kg": 2,  "zone": "lagos",  "fragile": False, "service": "standard"},
    {"id": "P2", "weight_kg": 35, "zone": "lagos",  "fragile": False, "service": "express"},
    {"id": "P3", "weight_kg": 12, "zone": "remote", "fragile": True,  "service": "standard"},
    {"id": "P4", "weight_kg": 8,  "zone": "remote", "fragile": False, "service": "express"},
    {"id": "P5", "weight_kg": 25, "zone": "lagos",  "fragile": True,  "service": "express"},
]

BASE_FEE = 1200

def evaluate(parcel, rules):
    total    = BASE_FEE
    applied  = []

    for rule in rules:
        field  = rule["field"]
        op     = rule["op"]
        target = rule["value"]
        actual = parcel[field]

        matched = False
        if op == ">":
            matched = actual > target
        elif op == "==":
            matched = actual == target

        if not matched:
            continue

    return (True, total, applied)