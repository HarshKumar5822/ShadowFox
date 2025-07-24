# Given values
radius = 84
pi = 3.14
water_per_sq_meter = 1.4

# Calculate the area of the pond
area = pi * radius * radius

# Calculate total water in liters
total_water = area * water_per_sq_meter

# Convert to integer (remove decimal)
total_water_no_decimal = int(total_water)

# Print the results
print("Area of the pond is:", area, "square meters")
print("Total water in the pond is:", total_water_no_decimal, "liters")
