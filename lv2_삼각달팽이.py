def solution(n):
    a = [[0]* n for _ in range(n)]
    num = 1
    cnt = 1
    x = 0
    y = 0
    for i in range(n,0,-1):
        for j in range(i):
            a[x][y] = num

            if cnt % 3 == 1:            
                if j != i-1:
                    x += 1
                else:
                    y += 1

            elif cnt % 3 == 2:
                if j != i-1:
                    y += 1
                else:
                    x -= 1
            else:
                if j != i-1:
                    x -= 1
                    y -= 1
                else:
                    x += 1
                    y -= 1
            num += 1
        cnt += 1
    answer = [y for x in a for y in x if y != 0]

    return answer