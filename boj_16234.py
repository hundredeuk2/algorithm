import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split(" "))
map_list = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0,0,-1,1], [1,-1,0,0]

days = 0
while True:
    visited = [[False] * n for _ in range(n)]
    moved = False  # 이번 날에 인구 이동(=연합 크기 >= 2)이 있었는가?

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue

            # BFS로 (i,c)에서 시작하는 연합 찾기
            q = deque([(i, j)])
            visited[i][j] = True
            union = [(i, j)]
            total_pop = map_list[i][j]

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if abs(map_list[x][y] - map_list[nx][ny]) in range(l,r+1):
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            union.append((nx, ny))
                            total_pop += map_list[nx][ny]

            # 연합 크기가 2 이상이면 평균으로 재분배
            if len(union) >= 2:
                moved = True
                new_pop = total_pop // len(union)
                for x, y in union:
                    map_list[x][y] = new_pop

    if not moved:
        break
    days += 1

print(days)