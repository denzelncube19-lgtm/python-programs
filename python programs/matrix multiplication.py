n = int(input("enter number  of rows "))
print("enter A matrix row by row seperated by space then press enter")
a= []
b = []
for i in range(n):
 row = input().strip().split()
 row = [int(x) for x in row] 
 a.append(row)
print("enter A matrix row by row seperated by space then press enter")
for i in range(n):
 row = input().strip().split()
 row = [int(x) for x in row] 
 b.append(row)
result = []
for i in range(len(a)):
   row = []
   for j in range(len(b[0])):
     total= 0
     for k in range(len(a[0])):
       total += a[i][k] * b[k][j]
     row.append(total)
   result.append(row)
for r in result: 
 print(r)

