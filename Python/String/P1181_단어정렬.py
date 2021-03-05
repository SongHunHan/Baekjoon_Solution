arr = []
setArr = []
for i in range(int(input())):
    arr.append(input())

arr = set(arr)

for i in arr:
    setArr.append((len(i),i))

setArr.sort()

for idx,word in setArr:
    print(word)