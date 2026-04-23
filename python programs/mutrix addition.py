a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
result = []
for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[i][j]+b[i][j])
    result.append(row)

for r in result:
    print(r)
 