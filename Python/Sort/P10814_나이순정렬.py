import sys
arr = []
for i in range(int(input())):
#   x,y = list(input().split())
    #arr.append([x,y])
    arr.append(list(sys.stdin.readline().split()))


arr.sort(key=lambda x:int(x[0]))
for i in arr:
    print(i[0],i[1])