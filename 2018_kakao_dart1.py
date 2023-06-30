def solution(dartResult):
    answer = 0
    stack = []
    s = ""
    dic = {"S":"1","D":"2","T":"3"}
    for dart in dartResult:
        if dart == "#":
            stack[-1] += "*-1"
        elif dart in dic.keys():
            s += "**"+dic[dart]
            stack.append(s)
            s = ""
        elif dart == "*":
            stack[-1] += "*2"
            if len(stack) <= 1 :
                continue
            stack[-2] += "*2"
        # numbers
        else:
            s += dart
    answer = '+'.join(stack)
    return eval(answer)