from itertools import combinations

n, total = input().split(" ")
num_list = [int(x) for x in input().split(" ")]

cnt = 0
for i in range(1, len(num_list)):
    if i == 1:
        for j in range(len(num_list)):
            if num_list[j] == total:
                print(num_list[j])
                cnt+=1
    for cob in combinations(num_list, i):
        if sum(cob) == int(total):
            cnt += 1
        
if sum(num_list) == int(total):
    cnt += 1
print(cnt)