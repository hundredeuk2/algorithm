n = int(input())
p_list = list(map(int,input().split()))
p_list.sort()

tmp_time = [p_list[0]]

for i in range(1,n):
    tmp_time.append(p_list[i] + tmp_time[-1])

    

print(sum(tmp_time))