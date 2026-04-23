# Count Vowels in a String
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in text if ch in vowels)
print(f"Number of vowels in '{text}': {count}")
