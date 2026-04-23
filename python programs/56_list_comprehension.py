# List Comprehension Examples
print("List Comprehension Demo")

# Squares of numbers 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares 1-10: {squares}")

# Even numbers 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even 1-20: {evens}")

# Flatten a matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [x for row in matrix for x in row]
print(f"Flattened matrix: {flat}")

# Words longer than 4 letters
sentence = input("Enter a sentence: ")
long_words = [w for w in sentence.split() if len(w) > 4]
print(f"Words longer than 4 chars: {long_words}")
