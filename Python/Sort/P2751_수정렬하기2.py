import sys
arr = []
for i in range(int(input())):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
    print(i)