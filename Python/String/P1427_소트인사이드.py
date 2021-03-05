"""
word = input()
arr =[]

for i in range(len(word)):
    arr.append(word[i])

arr.sort()
for i in range(-1,-len(arr)-1,-1):
    print(arr[i],end="")
"""
"""
n = list(map(int, input()))
n.sort(reverse=True)
for i in n:
    print(i,end='')
"""
n = input()
arr =[]
arr = list(map(int,str(n)))
arr.sort(reverse=True)
for i in arr:
    print(i,end="")