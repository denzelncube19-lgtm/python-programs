# Anagram Checker
word1 = input("Enter first word: ").lower().replace(" ", "")
word2 = input("Enter second word: ").lower().replace(" ", "")
if sorted(word1) == sorted(word2):
    print(f"'{word1}' and '{word2}' ARE anagrams!")
else:
    print(f"'{word1}' and '{word2}' are NOT anagrams.")
