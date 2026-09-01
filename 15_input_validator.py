raw_inputs = ["25", "0", "", "   ", "-15", "3.14", "hello", "₦2,500", "  42  ", "0.5"]

def validate_amount(raw):
    if raw.strip() == "":
        return (None, "Empty input")

    raw = raw.replace("₦", "").replace(",", "")

    try:
        parsed_input = float(raw)
    except ValueError:
        return (None, "Not a number")

    if parsed_input <= 0:
        return (None, "Must be positive")
    
    return (parsed_input, None)

accepted = 0
rejected = 0

for raw_input in raw_inputs:
    value, error = validate_amount(raw_input)
    print(f"{value}, {error}")

    if error is not None:
        rejected += 1
    else:
        accepted +=1

print(f"Accepted: {accepted}, Rejected: {rejected}")