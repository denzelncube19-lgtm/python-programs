#list comprehension
a = [1,2,3,4,5,6,7,8,9,10]
e = {i:i for i in a if i%2==0}
print(f"this is {e}dictionary",sep = "|")
d = [i*i for i in a ]
print(d)
n=7
m = [i*n for i in a]
print(m)
g=(i for i in a if i%2==0)
for i in g:
    print(i)