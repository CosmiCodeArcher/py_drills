# Use a for loop with range() to simulate exactly 5 grinding twists. 
# On each iteration, print "Twist 1 of 5", "Twist 2 of 5"

for count in range(1, 6):
    print(f"Twist {count} of 5")

# After the for loop finishes, 
# use a while loop to simulate filling a pepper jar to a target weight:

    # Start pepper_weight = 0.0 and target_weight = 5.0.
    # Each iteration adds 1.3 to pepper_weight and prints the current weight.
    # Loop continues while pepper_weight < target_weight.
    # After the loop ends naturally, print the final weight.

# Add one safety rule inside the while loop: 

    # if pepper_weight ever exceeds 6.0 (overshoot due to imprecise grinding), 
    # immediately break out of the loop and print "Overshoot! Stopping early."

pepper_weight = 0.0
target_weight = 5.0

while pepper_weight < target_weight:
    pepper_weight = pepper_weight + 1.3
    print(f"{pepper_weight}")
    if pepper_weight > 6.0:
        print("Overshoot! Stopping early.")
        break

print(f"{pepper_weight}")