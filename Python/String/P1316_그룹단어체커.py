n = int(input())
res = 0
for i in range(n):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+2:]:
                break
        else:
            res+=1
print(res)

'''
n = int(input())
res = n
for i in range(n):
    word = input()
    for j in range(1,len(word)):
        if word.find(word[j]) < word.find(word[j-1]):
            res-=1
            break
print(res)  
'''