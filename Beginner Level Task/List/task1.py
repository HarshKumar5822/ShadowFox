# 1. Create the initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Initial Justice League:", justice_league)

# 1. Count number of members
print("Number of members in Justice League:", len(justice_league))

# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl and Nightwing:", justice_league)

# 3. Move Wonder Woman to the beginning (make her leader)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)

# 4. Move a member between Aquaman and Flash to separate them
# First, find positions of Aquaman and Flash
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# We will move "Green Lantern" between them
justice_league.remove("Green Lantern")

# Find the new index of Aquaman and Flash again after removal
# (Flash index might change, so calculate again)
aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

# Insert Green Lantern between Aquaman and Flash
insert_position = min(aquaman_index, flash_index) + 1
justice_league.insert(insert_position, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)

# 5. Crisis happened — replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Justice League after crisis:", justice_league)

# 6. Sort the list alphabetically
justice_league.sort()
print("Sorted Justice League:", justice_league)

# BONUS: Who is the new leader?
print("New Leader (0th index):", justice_league[0])
