# Total jumping jacks required
total_jacks = 100
done_jacks = 0

# Loop to perform sets of 10
while done_jacks < total_jacks:
    # Do 10 jumping jacks
    done_jacks += 10
    print(f"\nYou did 10 jumping jacks. Total done: {done_jacks}")

    # If completed all
    if done_jacks == total_jacks:
        print("Congratulations! You completed the workout.")
        break

    # Ask if the user is tired
    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {done_jacks} jumping jacks.")
            break
        else:
            print(f"Keep going! {total_jacks - done_jacks} jumping jacks remaining.")
    else:
        print(f"Good job! {total_jacks - done_jacks} jumping jacks remaining.")
