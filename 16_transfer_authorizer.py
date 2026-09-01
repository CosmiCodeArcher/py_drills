def authorize(transfer):

    # Rule	                                                Failure message
    # Account is locked	                                    Account locked
    # PIN is wrong	                                        Incorrect PIN
    # Amount is not greater than zero	                    Invalid amount
    # International transfer to an unverified recipient	    International requires verified recipient
    # Unverified recipient, amount over 50000	            Unverified recipient limit is 50000
    # Amount exceeds balance	                            Insufficient funds
    # daily_used + amount exceeds 200000	                Daily limit exceeded

    # Test data:
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

    for transfer in transfers:
        if transfer['pin_ok'] == False:
            return (False, "Incorrect Pin")

        if transfer['locked'] == True:
            return (False, "Account locked")

        if transfer['amount'] <= 0:
            return (False, "Invalid Amount")