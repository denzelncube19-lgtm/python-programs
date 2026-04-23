# Flatten a Nested List
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
print(f"Nested list: {nested}")
flat = [item for sublist in nested for item in sublist]
print(f"Flattened  : {flat}")
