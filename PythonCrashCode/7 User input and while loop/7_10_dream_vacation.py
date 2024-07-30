# Initialize an empty list to store responses
vacation_destinations = []

# Start the polling process
print("Welcome to the Dream Vacation Poll!")

# Loop to gather responses
while True:
    # Prompt the user for their dream vacation destination
    destination = input("If you could visit one place in the world, where would you go? ")

    # Add the response to the list
    vacation_destinations.append(destination)

    # Ask if the user wants to continue
    continue_poll = input("Would you like to add another destination? (yes/no) ").lower()

    if continue_poll != 'yes':
        break

# Print the results
print("\nPoll Results:")
for i, destination in enumerate(vacation_destinations, 1):
    print(f"{i}. {destination}")
