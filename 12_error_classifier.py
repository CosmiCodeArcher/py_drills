import sys

errors = [
    {"file": "bank.py", "line": 12, "type": "SyntaxError", "message": "expected ':'"},
    {"file": "core.py", "line": 3, "type": "ZeroDivisionError", "message": "division by zero"},
    {"file": "util.py", "line": 45, "type": "IndentationError", "message": "expected an indented block"},
    {"file": "main.py", "line": 8, "type": "NameError", "message": "name 'balance' is not defined"},
    {"file": "parse.py", "line": 21, "type": "TabError", "message": "inconsistent use of tabs and spaces"},
]

compile_type_count = 0
runtime_type_count = 0

for error in errors:
    if error['type'] in ["SyntaxError", "IndentationError", "TabError"]:
        compile_type_count += 1
        category = "[compile-time]"
    else:
        runtime_type_count += 1
        category = "[runtime]"

    print(f"{error['file']}:{error['line']} - {error['type']} {category} - {error['message']}")

print(f"Compile-time: {compile_type_count}, Runtime: {runtime_type_count}")

if compile_type_count > 0:
    print(f"{compile_type_count} files(s) will not execute at all", file=sys.stderr)
    sys.exit(1)












# A hidden comment for learning reference:

# The one genuinely useful reframe here, worth internalizing: 
# if you find yourself writing a comment to explain confusing code, 
# first try to make the code clearer instead. Renaming discount → discounted_total 
# (from your very first drill) eliminated the need for a comment entirely — 
# better naming replaced explanation.

# Comments are for context the code genuinely can't express: 
# business rules, external constraints, why-not-the-obvious-approach decisions.