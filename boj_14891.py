import sys
input = sys.stdin.readline

def fix_index(curr, diff):
    return (curr + diff) % 8

def dfs(idx, direction, visited):
    visited[idx] = True

    if idx > 0 and not visited[idx - 1]:
        left_pole = gears[idx][fix_index(offset[idx], 6)]
        right_pole = gears[idx - 1][fix_index(offset[idx - 1], 2)]
        if left_pole != right_pole:
            dfs(idx - 1, -direction, visited)

    if idx < 3 and not visited[idx + 1]:
        right_pole = gears[idx][fix_index(offset[idx], 2)]
        left_pole = gears[idx + 1][fix_index(offset[idx + 1], 6)]
        if right_pole != left_pole:
            dfs(idx + 1, -direction, visited)

    offset[idx] = (offset[idx] - direction) % 8

gears = [list(map(int, input().strip())) for _ in range(4)]
offset = [0, 0, 0, 0]

K = int(input())
for _ in range(K):
    gear_num, direction = map(int, input().split())
    visited = [False] * 4
    dfs(gear_num - 1, direction, visited)

score = sum([2**i for i in range(4) if gears[i][offset[i]] == 1])

print(score)
