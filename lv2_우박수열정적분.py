def calculate(x):
    if x % 2 == 0:
        return x / 2
    return (x * 3) + 1

def solution(k, ranges):
    answer = []
    
    h = [float(k)]
    idx = float(k)
    while idx != 1:
        idx = calculate(idx)
        h.append(idx)
    
    value = []
    for i in range(len(h) - 1):
        s, e = h[i], h[i + 1]
        value.append((s + e) / 2)
    
    for x in ranges:
        s, e = x
        if e == 0:
            e = len(value)
        elif e < 0:
            e += len(value)

        if s > e:
            answer.append(-1.0)
        else:
            answer.append(sum(value[s:e]))
    
    return answer
