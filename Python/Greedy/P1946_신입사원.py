import sys
k = int(input())
for i in range(k):
    arr = []
    for j in range(int(input())):
        x,y = map(int,sys.stdin.readline().split())
        arr.append([x,y])
    arr.sort(key=lambda x:(x[0],x[1]))
    cmp = arr[0][1]
    cnt = 0
    for k in range(1,len(arr)):
        if arr[k][1]<cmp:
            cmp = arr[k][1]
            cnt+=1
    print(cnt+1)
    

