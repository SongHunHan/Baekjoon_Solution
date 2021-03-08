# arr = []
# setArr = []

# for i in range(int(input())):
#     arr.append(input())
# arr = set(arr)

# for i in arr:
#     setArr.append([len(i),i])

# setArr.sort()
# for length,word in setArr:
#     print(word)

v = list(set([input() for i in range(int(input()))]))
v.sort(key=lambda x:(len(x),x))
print("\n".join(v));