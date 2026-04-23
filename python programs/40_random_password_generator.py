# Random Password Generator
import random
import string
length = int(input("Enter desired password length: "))
use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

chars = string.ascii_lowercase
if use_upper: chars += string.ascii_uppercase
if use_digits: chars += string.digits
if use_special: chars += string.punctuation

password = ''.join(random.choice(chars) for _ in range(length))
print(f"\nGenerated Password: {password}")
