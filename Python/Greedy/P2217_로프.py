import sys
n= int(input())
k = []
for i in range(n):
    k.append(int(sys.stdin.readline()))

k.sort()
res = []
for i in range(n):
    res.append(int(k[i]*(n-i)))
print(max(res))