str = input()

for i in range(len(str)):
    print(str[i],end="")
    if(i%10==9):
        print()
        