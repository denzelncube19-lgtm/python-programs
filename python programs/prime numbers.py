n = int(input())
i = 2
flag =0 
for i in range( 2 , n//2 + 1):
    if n%i == 0:
     flag+=1
if flag:
   print("not prime")
else:
   print("prime")
