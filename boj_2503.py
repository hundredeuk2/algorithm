from itertools import permutations

n = int(input())
tries = [input().split(" ") for _ in range(n)]

cnt = 0
for per in permutations(range(1,10), 3):
    status = True
    
    for num, st, bl in tries:
        true_st = true_bl = 0
        
        for i in range(3):
            if str(per[i]) == num[i]:
                true_st += 1
            elif str(per[i]) in num:
                true_bl += 1
        
        if true_st != int(st) or true_bl != int(bl):
            status = False
            break
    if status:
        cnt +=1
print(cnt)