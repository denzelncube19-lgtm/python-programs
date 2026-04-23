class timeconverter:
    def __init__(self,seconds):
         self.seconds= seconds

    def convert(self):
         hours = self.seconds // 3600
         minutes = (self.seconds%3600) // 60
         seconds = self.seconds % 60
         return hours , minutes, seconds
    
    def display(self):
         h , m , s = self.convert()
         print(f" hours : {h},minutes: {m}, seconds{s}")


time = int(input("enter number of seconds"))   
case1 = timeconverter(time)
case1.display()