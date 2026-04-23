# Palindrome Checker
text = input("Enter a word or number: ").lower().replace(" ", "")
if text == text[::-1]:
    print(f"'{text}' is a PALINDROME")
else:
    print(f"'{text}' is NOT a palindrome")
