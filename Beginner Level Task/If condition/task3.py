# Define city lists for each country
australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Ask the user to enter two cities
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

# Check which country each city belongs to
country1 = ""
country2 = ""

if city1 in australia:
    country1 = "Australia"
elif city1 in uae:
    country1 = "UAE"
elif city1 in india:
    country1 = "India"

if city2 in australia:
    country2 = "Australia"
elif city2 in uae:
    country2 = "UAE"
elif city2 in india:
    country2 = "India"

# Compare both countries
if country1 != "" and country1 == country2:
    print(f"Both cities are in {country1}")
elif country1 != "" and country2 != "":
    print("They don't belong to the same country")
else:
    print("One or both cities are not recognized.")
