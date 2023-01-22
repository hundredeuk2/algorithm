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
        arr.append(num_list[i])
        dfs(i+1)
        arr.pop()

dfs(0)