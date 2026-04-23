import math
n = input()
mult = 0
add = sum(int(d) for d in n)
mult = math.prod(int(d)for d in n)
if add == mult: 
 print ("spy number")
else:
 print("not spy")