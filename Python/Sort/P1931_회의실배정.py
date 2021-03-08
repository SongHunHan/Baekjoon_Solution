#import sys
#input=sys.stdin.readline
n = int(input())
v = []
for i in range(n):
    x,y = map(int,input().split())
    v.append([x,y])

#s.sort(key =lambda x:(x[1],x[0]))
v = sorted(v,key=lambda v:v[0])
v = sorted(v,key=lambda v:v[1])

cnt = 0
nowPlace = 0
for first,second in v:
    if nowPlace <=first:
        cnt+=1
        nowPlace = second
print(cnt)