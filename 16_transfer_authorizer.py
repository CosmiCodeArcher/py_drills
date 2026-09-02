transfers = [
    {"id": "T1", "amount": 15000,  "balance": 90000, "daily_used": 0,
    "pin_ok": True,  "locked": False, "international": False, "verified": True},
    {"id": "T2", "amount": 0,      "balance": 90000, "daily_used": 0,
    "pin_ok": True,  "locked": False, "international": False, "verified": True},
    {"id": "T3", "amount": 60000,  "balance": 90000, "daily_used": 0,
    "pin_ok": True,  "locked": False, "international": True,  "verified": False},
    {"id": "T4", "amount": 60000,  "balance": 90000, "daily_used": 0,
    "pin_ok": True,  "locked": False, "international": False, "verified": False},
    {"id": "T5", "amount": 10000,  "balance": 90000, "daily_used": 0,
    "pin_ok": True,  "locked": False, "international": True,  "verified": False},
    {"id": "T6", "amount": 150000, "balance": 300000, "daily_used": 80000,
    "pin_ok": True,  "locked": False, "international": False, "verified": True},
    {"id": "T7", "amount": 5000,   "balance": 1000,  "daily_used": 0,
    "pin_ok": False, "locked": True,  "international": False, "verified": True},
]

def authorize(transfer):
    if not transfer['pin_ok']:
        return (False, "Incorrect Pin")

    if transfer['locked']:
        return (False, "Account locked")

    if transfer['amount'] <= 0:
        return (False, "Invalid Amount")

    if transfer['amount'] > transfer['balance']:
        return (False, "Insufficient funds")

    if (transfer['daily_used'] + transfer['amount']) > 200000:
        return (False, "Daily limit exceeded")

    if (transfer['international']) and (not transfer['verified']):
        return (False, "International requires verified recipient")

    if (not transfer['verified']) and (transfer['amount'] > 50000):
        return (False, "Unverified recipient limit is 50000")

    return (True, "Approved")

for transfer in transfers:
    result, reason = authorize(transfer)
    
    if not result:
        print(f"{transfer['id']} Rejected: {reason}")
    else:
        print(f"{transfer['id']} {reason}")

# Hand predictions:
    #   T5 -> "International requires verified recipient"
    #   T7 -> "Incorrect Pin"