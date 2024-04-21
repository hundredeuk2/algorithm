def n_jin(n, q):
    str_list = "0123456789ABCDEFG"
    rev_base = ''
    if n == 0:
        return "0"
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str_list[mod]

    return rev_base[::-1] 

def solution(n, t, m, p):
    answer = ''
    l = ""
    i = 0
    while len(l) < t*m:
        l += n_jin(i,n)
        i += 1
        
    for i in range(p-1,len(l),m):
        answer += l[i]
    return answer[:t]