class feet_to_inch_converter:
    def __init__(self, feet):
        self.feet = feet

    def convert_to_feet(self):
        inch = self.feet * 12
        return inch
    
    def display(self):
        inch = self.convert_to_feet()
        print(f"inches {inch}")

inch = int(input("enter number of feet  "))
feet1 = feet_to_inch_converter(inch)
feet1.display()



