import re

def solution(str1, str2):
    answer = 0
    pattern = re.compile("[a-zA-Z]+$")
    double_1 = list(filter(pattern.match,[str1[i:i+2].lower() for i in range(len(str1)-1)]))
    double_2 = list(filter(pattern.match,[str2[i:i+2].lower() for i in range(len(str2)-1)]))
    same = []
    for st in double_1:
        if st in double_2:
            same.append(st)
            double_2.remove(st)
    double_1.extend(double_2)
    
    if len(same) == len(double_1):
        return 65536
    return  int(len(same) / len(double_1) * 65536)