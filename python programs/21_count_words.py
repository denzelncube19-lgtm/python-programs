# Word Frequency Counter
text = input("Enter a sentence: ")
words = text.lower().split()
freq = {}
for word in words:
    word = word.strip(".,!?")
    freq[word] = freq.get(word, 0) + 1
print("\nWord Frequencies:")
for word, count in sorted(freq.items()):
    print(f"  {word}: {count}")
