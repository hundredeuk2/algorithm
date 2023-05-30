def solution(today, terms, privacies):
    answer = []
    diff_list = []
    
    term = {}
    for x in terms:
        tmp = x.split(" ")
        term[tmp[0]] = int(tmp[1])
        
    today = today.split(".")
    for i in range(len(privacies)):
        tmp = privacies[i].split(" ")
        t = tmp[0].split(".")
        value = [(int(today[0])-int(t[0]))*12, int(today[1])-int(t[1]), (int(today[2])-int(t[2])) / 28]

        if term[tmp[1]] <= sum(value):
            answer.append(i+1)
    return answer