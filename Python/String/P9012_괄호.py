k = int(input())
for i in range(k):
    str = input()
    cnt = 0
    for j in range(len(str)):
        if str[j]=="(":
            cnt = cnt+1
        elif str[j] ==")":
            cnt = cnt-1

        if cnt<0:
            break
    if cnt==0:
        print("YES")
    else:
        print("NO")