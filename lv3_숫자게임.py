def solution(A, B):
    B.sort(reverse=True)
    A.sort(reverse=True)
    answer = 0
    j = 0
    for i in range(len(A)):
        if A[i] < B[j]:
            answer += 1
            j += 1
            continue
    return answer