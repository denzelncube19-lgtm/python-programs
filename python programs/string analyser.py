s= input("enter string here")
v = 0
d = 0
c = 0
for ch in s:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E"   or ch == "I" or ch == "O" or ch == "U":
      v +=1  
    elif ch.isdigit():
       d+=1
    else:
       c +=1
print("vowels are:", v)   
print("digits are:", d) 
print("consonents are:", c) 
       
         

 

 