def solution(skill, skill_trees):
    answer = -1
    cnt = 0
    for tree in skill_trees:
        visited = [int(1e9)] * len(skill)
        for s in set(skill) - (set(skill) - set(tree)):
            visited[skill.index(s)] = tree.index(s)
        tmp = visited[0]
        status = True
        for i in range(1, len(visited)):
            if tmp > visited[i] :
                status = False
                break
            tmp = visited[i]

        if status:
            cnt += 1
    
    return cnt