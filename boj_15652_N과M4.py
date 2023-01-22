import sys
input = sys.stdin.readline

n,m = map(int, input().split())

num_list = [i+1 for i in range(n)]

arr = []

def dfs(s) :
    if len(arr) == m:
        print(*arr)
        return
    for i in range(n):
        if len(arr) != 0:
            if arr[-1] > num_list[i]:
                continue
        arr.append(num_list[i])
        dfs(s+1)
        arr.pop()

dfs(0)