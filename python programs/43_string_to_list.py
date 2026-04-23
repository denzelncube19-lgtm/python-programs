# String Manipulation - Split and Join
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Words: {words}")
print(f"Number of words: {len(words)}")
print(f"Sorted words: {sorted(words)}")
print(f"Reversed sentence: {' '.join(reversed(words))}")
