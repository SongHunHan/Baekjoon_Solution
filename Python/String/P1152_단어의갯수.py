str = input()
length = len(str)
cnt = 0
if str== " ":
    print(0)
else:
    for i in range(1,length-1):
        if str[i]==" ":
            cnt+=1
    print(cnt+1)