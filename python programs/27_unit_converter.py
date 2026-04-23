# Unit Converter (Length)
print("Length Converter")
print("1. Km to Miles  2. Miles to Km  3. Meters to Feet  4. Feet to Meters")
choice = input("Choose: ")
if choice == '1':
    km = float(input("Enter km: "))
    print(f"{km} km = {km * 0.621371:.4f} miles")
elif choice == '2':
    mi = float(input("Enter miles: "))
    print(f"{mi} miles = {mi * 1.60934:.4f} km")
elif choice == '3':
    m = float(input("Enter meters: "))
    print(f"{m} m = {m * 3.28084:.4f} feet")
elif choice == '4':
    ft = float(input("Enter feet: "))
    print(f"{ft} feet = {ft * 0.3048:.4f} meters")
