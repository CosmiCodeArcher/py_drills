queue = [
    {"id": "K1", "priority": "high",   "difficulty": 2},
    {"id": "K2", "priority": "low",    "difficulty": 5},
    {"id": "K3", "priority": "high",   "difficulty": 1},
    {"id": "K4", "priority": "medium", "difficulty": 4},
    {"id": "K5", "priority": "low",    "difficulty": 3},
    {"id": "K6", "priority": "high",   "difficulty": 6},
]

MAX_ATTEMPTS = 3
DAILY_CAPACITY = 12

# Rules.

# A ticket is resolved when accumulated effort reaches its difficulty. 
# Each attempt adds effort equal to the attempt number — attempt 1 adds 1, 
# attempt 2 adds 2, attempt 3 adds 3. 
# So difficulty 5 resolves on attempt 3 (1+2+3=6 ≥ 5); 
# difficulty 6 also resolves on attempt 3; 
# difficulty 7 would never resolve within MAX_ATTEMPTS.

# Every attempt costs 1 unit of daily capacity, whether or not it resolves the ticket. 
# When capacity is exhausted, stop processing entirely — remaining tickets are untouched, not failed.

# A ticket that hits MAX_ATTEMPTS without resolving is abandoned as failed. 
# Capacity still gets spent on those attempts.