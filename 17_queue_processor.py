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
daily_cap = DAILY_CAPACITY

out_of_capacity = False

for idx, ticket in enumerate(queue, start=1):
    attempts = 0
    effort = 0
    difficulty = ticket["difficulty"]


    while True:

        if daily_cap <= 0:
            out_of_capacity = True
            break

        attempts += 1
        effort += attempts
        daily_cap -= 1
        capacity_used += 1

        if effort >= difficulty:
            print(f"{idx}. {ticket['id']} resolved after {attempts} attempts (effort {effort} / {difficulty})")
            resolved += 1
            break

        if attempts == MAX_ATTEMPTS:
            print(f"{idx}. {ticket['id']} abandoned after {attempts} attempts (effort {effort} / {difficulty})")
            abandoned += 1
            break

    if out_of_capacity:
        break
        
never_reached = len(queue) - resolved - abandoned

print(f"Resolved count: {resolved}, Abandoned count: {abandoned}, Tickets never reached: {never_reached}, Capacity used: {capacity_used}")