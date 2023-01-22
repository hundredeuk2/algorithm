from collections import deque

n = int(input())
now_list = deque([x for x in range(1,n+1)])
drop_list = ""

while len(now_list)!= 1:
    tmp = now_list.popleft()
    drop_list += f"{tmp} "
    tmp = now_list.popleft()
    now_list.append(tmp)
    
print(drop_list + str(now_list[0]))