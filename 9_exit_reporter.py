results = [
    {"name": "mkdir ai_projects", "exit_code": 0},
    {"name": "cd ai_projects", "exit_code": 0},
    {"name": "python broken_recipe.py", "exit_code": 1},
    {"name": "touch core.py", "exit_code": 0},
    {"name": "python missing_file.py", "exit_code": 2},
]

count = 0

for d in results:
    count += 1
    if d['exit_code'] == 0:
        print(f"{d['name']} - OK")
    else:
        print(f"{d['name']} - FAILED (exit {d['exit_code']})")
        print("Chain aborted.")
        break

print(f"Commands run: {count}")