n = int(input())
fixedNumber = n
cnt =0

while True:
    ten = n//10
    one = n%10
    next = ten+one
    cnt+=1
    n = one*10 + (next%10)
    if n==fixedNumber:
        break

print(cnt)