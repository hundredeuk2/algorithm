n = int(input())
num_l = list(map(int, input().split()))

answer = 0
for num in num_l:
    tmp=[]
    for j in range(1,num+1):
        if num % j == 0:
            tmp.append(j)
    if len(tmp) == 2:
        answer += 1
        
print(answer)