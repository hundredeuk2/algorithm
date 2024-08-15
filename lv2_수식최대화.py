from itertools import permutations

def solution(expression):
    answer = 0
    yeonsan = "*-+"
    perm = permutations(yeonsan, len(yeonsan))
    for yeonsan in perm:

        tmp = ""
        n_expression = []
        for x in expression:
            if x not in yeonsan:
                tmp += x
            else:
                n_expression.append(tmp)
                n_expression.append(x)
                tmp =""
        n_expression.append(tmp)

        for now in yeonsan:
            while True:
                if now not in n_expression:
                    break
                idx = n_expression.index(now)
                tmp = eval("".join(n_expression[idx-1:idx+2]))
                n_expression = n_expression[:idx-1] + [str(eval("".join(n_expression[idx-1:idx+2])))] + n_expression[idx+2:]
        tmp = int(n_expression.pop())
        answer = max(answer, abs(tmp))
    return answer