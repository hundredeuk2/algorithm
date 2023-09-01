import sys
sys.setrecursionlimit(10000)  # Increase recursion limit if necessary

def dfs(now, parent, usado, threshold):
    result = 0
    # 시작점은 카운트하지 않습니다.
    if parent != 0 and usado >= threshold:
        result += 1

    for node in graph[now]:
        n_node, n_cost = node
        if n_node != parent:
            # 재귀 함수를 통해 result 값을 업데이트합니다.
            result += dfs(n_node, now, min(usado, n_cost), threshold)

    return result

if __name__ == "__main__":
    n, q = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    for _ in range(q):
        threshold, v = map(int, input().split())
        print(dfs(v, 0, float('inf'), threshold))