arr = []
for i in range(int(input())):
    x = int(input())
    if x!=0:
        arr.append(x)
    else:
        arr.pop()

print(sum(arr))