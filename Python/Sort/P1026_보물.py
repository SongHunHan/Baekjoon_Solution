import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
sum = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    sum+=b[i]*a[i]
print(sum)