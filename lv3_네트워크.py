def find(node, root):
    if root[node] == node:
        return node
    return find(root[node], root)

def union(a,b, root):
    n_a = find(a,root)
    n_b = find(b,root)
    
    if n_a < n_b :
        root[n_b] = n_a
    else:
        root[n_a] = n_b


def solution(n, computers):
    root = [i for i in range(n+1)]
    for row in range(n):
            for col in range(n):
                if row == col:
                    continue

                if computers[row][col]:
                    union(row+1, col+1, root)

    ans = set()
    for i in range(1,n+1):
        tmp = find(root[i], root)
        ans.add(tmp)
    return len(ans)