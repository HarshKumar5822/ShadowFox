# Given values
distance = 490  # in meters
time_minutes = 7

# Convert time to seconds
time_seconds = time_minutes * 60

# Calculate speed in meters per second
speed = distance / time_seconds

# Remove decimal point by converting to integer
speed_no_decimal = int(speed)

# Print the result
print("Your speed is:", speed_no_decimal, "meters per second")
