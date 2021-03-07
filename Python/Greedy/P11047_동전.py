n,k = map(int,input().split())

arr = []
cnt = 0
for i in range(int(n)):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in arr:
    if k==0:
        break
    cnt +=k//i
    k%=i
        
print(cnt)