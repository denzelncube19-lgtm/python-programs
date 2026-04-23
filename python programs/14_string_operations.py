# String Operations
text = input("Enter a string: ")
print(f"Original    : {text}")
print(f"Uppercase   : {text.upper()}")
print(f"Lowercase   : {text.lower()}")
print(f"Title Case  : {text.title()}")
print(f"Length      : {len(text)}")
print(f"Word count  : {len(text.split())}")
print(f"Reversed    : {text[::-1]}")
