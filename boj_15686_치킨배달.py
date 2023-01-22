from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_list = []
house_list = []
chicken_list = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            house_list.append([i,j])
        elif tmp[j] == 2:
            chicken_list.append([i,j])
    map_list.append(tmp)
    
def distance(house, chicken):
    return abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])


answer = int(1e9)

    
for cob in combinations(chicken_list,m):
    tmp = 0
    for house in house_list:
        m_tmp = int(1e9)
        for x in cob:
            m_tmp = min(m_tmp, distance(house,x))
        tmp += m_tmp
    answer = min(answer, tmp)
print(answer)