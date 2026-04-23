import math
n = int(input())
root = int(math.sqrt(n))
if root * root == n:
    print("perfect square")
else:
    print("not perfect square")
    