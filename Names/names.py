names = []

# Prompt the user to enter names
while True:
    name = input("Enter a name (or type 'done' to finish): ")
    
    # Check if the user wants to stop entering names
    if name.lower() == 'done':
        break
    
    # Append the entered name to the list
    names.append(name)

# Remove duplicates by converting the list to a set, then back to a list
unique_names = list(set(names))

# Sort the names in alphabetical order
unique_names.sort()

# Display the list of unique names
print("\nList of unique names entered (sorted):")
print(unique_names)