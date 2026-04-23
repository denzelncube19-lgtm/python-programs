# Grade Calculator
subjects = int(input("How many subjects? "))
total = 0
for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks
avg = total / subjects
print(f"\nTotal Marks : {total}")
print(f"Average     : {avg:.2f}")
if avg >= 90:
    grade = 'A+'
elif avg >= 80:
    grade = 'A'
elif avg >= 70:
    grade = 'B'
elif avg >= 60:
    grade = 'C'
elif avg >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f"Grade       : {grade}")
