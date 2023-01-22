import sys
input = sys.stdin.readline
from collections import Counter

N,M = map(int,input().split())

N_list = []
M_list = []
for _ in range(N):
    name = input().strip()
    N_list.append(name)

for _ in range(M):
    name = input().strip()
    M_list.append(name)

A = Counter(N_list) & Counter(M_list)
answer = []
for name in A.elements():
    answer.append(name)
answer.sort()
print(len(answer),*answer,sep='\n')