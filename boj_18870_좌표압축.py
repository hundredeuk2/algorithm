import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
org_list = list(map(int, input().split()))
set_list = sorted(list(set(org_list)))
dic = {}
i = 0

for num in set_list:
    dic[num] = i
    i += 1

answer = []

for number in org_list:
    tmp = dic[number]
    answer.append(tmp)
    
print(*answer)