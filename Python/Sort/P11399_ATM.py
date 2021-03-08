n= int(input())
arr = list(map(int,input().split()))

arr.sort()
sum = 0
next = 0
for i in arr:
    next +=i
    sum +=next

print(sum)