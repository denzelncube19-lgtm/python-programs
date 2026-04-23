n = int(input())
org = n
arm = 0
while(n>0):
    digit = (n%10)**3
    arm = arm + digit
    n //=10
if org == arm:
 print("armstrong number")
else:
    print("not an armstrong number")