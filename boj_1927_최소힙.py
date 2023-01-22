import heapq
import sys
input = sys.stdin.readline
n = int(input())

h = []
answer = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(h) == 0:
            answer.append(0)
        else:
            answer.append(heapq.heappop(h))
    else:
        heapq.heappush(h, num)
print(*answer,sep='\n')