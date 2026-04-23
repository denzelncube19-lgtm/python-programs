# Number to Words (1-20)
ones = ["", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
        "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty"]
num = int(input("Enter a number (1-20): "))
if 1 <= num <= 20:
    print(f"{num} in words: {ones[num]}")
else:
    print("Number out of range!")
