# Mini Quiz Game
questions = [
    {"q": "What is the capital of France?", "a": "paris"},
    {"q": "Which planet is closest to the sun?", "a": "mercury"},
    {"q": "What is 15 x 15?", "a": "225"},
    {"q": "Who wrote Romeo and Juliet?", "a": "shakespeare"},
    {"q": "What is the boiling point of water in Celsius?", "a": "100"},
]
print("Welcome to the Mini Quiz Game!\n")
score = 0
for i, item in enumerate(questions, 1):
    print(f"Q{i}: {item['q']}")
    ans = input("Your answer: ").strip().lower()
    if ans == item['a']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Answer was: {item['a']}\n")
print(f"Final Score: {score}/{len(questions)}")
if score == len(questions):
    print("Perfect score! Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
