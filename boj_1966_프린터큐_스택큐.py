from collections import deque

n = int(input())
for _ in range(n):
    
    m, idx = map(int,input().split(' '))
    q_list = deque(list(map(int, input().split(' '))))
    
    cnt = 0
    while True:
        max_val = max(q_list)
        tmp = q_list.popleft()
        if tmp == max_val:
            cnt += 1
            if idx == 0:
                break
            else :
                idx -= 1
        else:
            q_list.append(tmp)
            if idx == 0:
                idx = len(q_list)-1
            else:
                idx -= 1
    print(cnt)