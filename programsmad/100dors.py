#!/usr/bin/python3

# List of all doors (+1 to work properly) and they state ("False" = closed].
all_doors = [False] * 101

# Count of passing the corridor (100 times, and pass by 1).
for corridor in range(1,101,1):
    # Count of passing through the exact door from all doors list ("all_doors") by N ("corridor") times.
    for i in range(0,len(all_doors),corridor):
        # Change the state of door (if passed one is touched) to "open" or "not open" (as well) and display as numbers (from "i" range).
        open = all_doors[i]
        all_doors[i] = not open

# The results.
print("The following doors are open: ", end="")     # Display number of the exact doors.
for i in range(0,len(all_doors)):
    if all_doors[i]:                            # Only if the door state is set to the "open".
        print(str(i), end=", ")                 # Print the result as string (number of door).
print("\a\a.")