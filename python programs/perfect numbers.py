n = int(input())
i=1
sum = 0
while(i<n):
 if n%i == 0:
   sum +=i
 i +=1
if sum == n:
 print("perfect number ")
else:
 print("not perfect number")    