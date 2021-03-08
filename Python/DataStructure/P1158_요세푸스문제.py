n,k = map(int,input().split())
arr = [i for i in range(1,n+1)]
res =[]

delNumber = 0
for i in range(n):
    delNumber = delNumber + k -1
    if delNumber >= len(arr):
        delNumber = delNumber %len(arr)
    res.append(str(arr.pop(delNumber)))

print("<",", ".join(res)[:],">",sep='')