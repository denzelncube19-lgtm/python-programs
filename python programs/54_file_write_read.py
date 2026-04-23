# File Write and Read Demo
filename = "sample.txt"

# Write to file
with open(filename, 'w') as f:
    lines = int(input("How many lines to write? "))
    for i in range(lines):
        line = input(f"Line {i+1}: ")
        f.write(line + "\n")
print(f"Written to '{filename}'")

# Read from file
print("\nReading file contents:")
with open(filename, 'r') as f:
    for i, line in enumerate(f, 1):
        print(f"  {i}: {line}", end="")

import os
os.remove(filename)
