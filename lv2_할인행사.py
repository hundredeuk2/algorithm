from collections import Counter

def solution(want, number, discount):
    answer = 0
    total = len(discount) - sum(number)
    want_dict = {k:v for k,v in zip(want, number)}
    cnt = 0
    while True:
        if cnt == total+1:
            break
        tmp_dict =  Counter(discount[cnt:10+cnt])
        status = True
        for key in want:
            if tmp_dict[key] < want_dict[key] :
                status = False
                break
        if status:
            answer += 1
        cnt += 1
    return answer