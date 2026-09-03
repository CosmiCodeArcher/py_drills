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

resolved = 0
abandoned = 0
never_reached = 0
capacity_used = 0

for idx, ticket in enumerate(queue, start=1):
    attempts = 0
    effort = 0

    while True:
        attempts += 1
        effort += attempts
        DAILY_CAPACITY -= 1
        capacity_used += 1
        difficulty = ticket["difficulty"]

        if effort == difficulty:
            print(f"{ticket["id"]} resolved after {attempts} attempts (effort {effort} / {difficulty})")
            resolved += 1

        if attempts == MAX_ATTEMPTS:
            print(f"abandoned after {attempts} attempts (effort {effort} / {difficulty})")
            abandoned += 1
            continue

        if DAILY_CAPACITY == 0:
            break

    if DAILY_CAPACITY == 0:
        never_reached = len(queue) - idx
        break

print(f"Resolved count: {resolved}, Abandoned count: {abandoned}, Tickets never reached: {never_reached}, Capacity used: {capacity_used}")