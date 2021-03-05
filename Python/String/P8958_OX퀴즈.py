n = int(input())
for i in range(n):
    str = input()
    cnt = 0
    sum = 0
    for j in range(len(str)):
        if str[j]=="O":
            cnt+=1
            sum +=cnt
        else:
            cnt = 0
    print(sum)