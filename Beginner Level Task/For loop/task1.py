import random

# Number of times to roll the die
rolls = 20

# Counters
count_six = 0
count_one = 0
count_two_sixes_in_a_row = 0

# Variable to remember the previous roll
previous_roll = 0

# Simulate rolling the die
for i in range(rolls):
    roll = random.randint(1, 6)  # Random number between 1 and 6
    print(f"Roll {i+1}: {roll}")

    # Count 6s
    if roll == 6:
        count_six += 1

    # Count 1s
    if roll == 1:
        count_one += 1

    # Check for two 6s in a row
    if previous_roll == 6 and roll == 6:
        count_two_sixes_in_a_row += 1

    # Update previous roll
    previous_roll = roll

# Print the results
print("\nResults:")
print("Number of times rolled a 6:", count_six)
print("Number of times rolled a 1:", count_one)
print("Number of times two 6s appeared in a row:", count_two_sixes_in_a_row)
