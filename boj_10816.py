n = int(input())
n_list = [int(x) for x in input().split(" ")]
m = int(input())
m_list = [int(x) for x in input().split(" ")]

n_dict = {k:0 for k in set(n_list)}
for num in n_list:
    n_dict[num] += 1

new_list = []
for x in m_list:
    if x in n_dict.keys():
        new_list.append(n_dict[x])
    else:
        new_list.append(0)
print(*new_list)