# Hardcode three string "inputs": age_input = "17", has_ticket_input = "yes", has_guardian_input = "no"

age_input = "17"
has_ticket_input = "yes"
has_guardian_input = "no"

# Safely convert age_input to an integer using try/except — if the conversion fails (pretend a bad value could arrive), 
# print "Invalid age input" and stop that path; otherwise continue

try:
    age_input = int(age_input)
except ValueError:
    print("Invalid age input")

# Convert has_ticket_input and has_guardian_input into actual booleans (True/False) 
# — your call on how, but think about what a clean way to do that looks like given they're plain "yes"/"no" strings.

has_ticket_input = (has_ticket_input == "yes")
has_guardian_input = (has_guardian_input == "yes")

# Using an if/elif/else chain combined with logical operators (and/or/not), determine entry status:
# If age >= 18 and has a ticket → "Entry granted: adult with ticket"
# elif age < 18 and has a ticket and has a guardian → "Entry granted: minor with ticket and guardian"
# elif has a ticket and not has_guardian and age < 18 → "Entry denied: minor needs a guardian"
# else → "Entry denied: no valid ticket"

if age_input >= 18 and has_ticket_input:
    print("Entry granted: adult with ticket")
elif age_input < 18 and has_ticket_input and has_guardian_input:
    print("Entry granted: minor with ticket and guardian")
elif has_ticket_input and not has_guardian_input and age_input < 18:
    print("Entry denied: minor needs a guardian")
else:
    print("Entry denied: no valid ticket")