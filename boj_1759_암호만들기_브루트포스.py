from itertools import combinations

L, C = map(int, input().split(' '))
moum = ['a','e','i','o','u']
letter_list = sorted(list(map(str,input().split(' '))))

cob_list = list(combinations(letter_list,L))

for cob in cob_list:
    cnt = 0
    for mo in moum:
        if mo in cob:
            cnt += 1
    if L - cnt <= 1 or cnt == 0:
        continue
    else: 
        print(*cob,sep='')