from collections import Counter

n = int(input())
matryoshika = list(map(int, input().split(" ")))
matryoshika_dict = Counter(matryoshika)
matryoshika_dict = dict(sorted(matryoshika_dict.items()))

key_list = list(matryoshika_dict.keys())
cnt = 0

while True:
    idx_list = []
  
    if len(key_list) <= 0:
        break
  
    for k in key_list:
        matryoshika_dict[k] -= 1
        if matryoshika_dict[k] <= 0:
            idx_list.append(k)
    cnt += 1
  
    if idx_list:
        for l in idx_list:
            key_list.pop(key_list.index(l))

print(cnt)