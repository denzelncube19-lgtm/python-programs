# Character Counter
text = input("Enter a string: ")
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
spaces = sum(c.isspace() for c in text)
special = len(text) - letters - digits - spaces
print(f"Letters : {letters}")
print(f"Digits  : {digits}")
print(f"Spaces  : {spaces}")
print(f"Special : {special}")
print(f"Total   : {len(text)}")
