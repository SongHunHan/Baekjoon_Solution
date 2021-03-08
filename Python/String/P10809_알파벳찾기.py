word = input()
idx = 0
arr = [-1]*26
for i in word:
    if arr[ord(i)-97]==-1:
        arr[ord(i)-97] = idx
    idx +=1

for i in range(26):
    print(arr[i])