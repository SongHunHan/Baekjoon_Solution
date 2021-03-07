n = input()
arr = n.split("-")

res = []
for i in arr:
    sum = 0
    s = i.split("+")
    for j in s:
        sum += int(j)
    res.append(sum)

firstNumber = res[0]
for i in range(1,len(res)):
    firstNumber-=res[i]

print(firstNumber)