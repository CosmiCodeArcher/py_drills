import sys

entries = [
    {"message": "Order 1 processed", "level": "info"},
    {"message": "Payment gateway timeout", "level": "error"},
    {"message": "Order 2 processed", "level": "info"},
    {"message": "Invalid card number", "level": "error"},
    {"message": "Order 3 processed", "level": "info"},
]

error_count = 0

for entry in entries:
    if entry['level'] == "info":
        print(f"{entry['message']}")
    else:
        error_count += 1
        print(f"{entry['message']}", file=sys.stderr)

if error_count > 0:
    print(f"{error_count} errors occurred", file=sys.stderr)
    sys.exit(1)
else:
    print("All clean")

# Terminal tests
# python log_splitter.py
# python log_splitter.py > info.txt
# python log_splitter.py 2> errors.txt