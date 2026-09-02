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
        return (False, f"{transfer['id']}: Incorrect Pin")

    if transfer['locked']:
        return (False, f"{transfer['id']}: Account locked")

    if transfer['amount'] <= 0:
        return (False, f"{transfer['id']}: Invalid Amount")

    if transfer['amount'] > transfer['balance']:
        return (False, f"{transfer['id']}: Insufficient funds")

    if (transfer['daily_used'] + transfer['amount']) > 200000:
        return (False, f"{transfer['id']}: Daily limit exceeded")

    if (not transfer['verified']) and (transfer['amount'] > 50000) and (not transfer['international']):
        return (False, f"{transfer['id']}: Unverified recipient limit is 50000")

    if (transfer['international']) and (not transfer['verified']):
        return (False, f"{transfer['id']}: International requires verified recipient")

    return (True, f"{transfer['id']}: Approved")

for transfer in transfers:
    result, reason = authorize(transfer)
    
    if not result:
        print(f"Rejected: {reason}")
    else:
        print(f"{reason}")

# Hand predictions:
    #   T5 -> "International requires verified recipient"
    #   T7 -> "Incorrect Pin"