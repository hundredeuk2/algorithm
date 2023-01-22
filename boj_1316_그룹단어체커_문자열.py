n = int(input())
word_l = []
for _ in range(n):
    word_l.append(str(input()))

cnt = 0

for word in word_l:
    slic_word = list(map(str,word))
    set_l = list(set(slic_word))
    q = [slic_word[0]]
    for l in slic_word:
        b = q[-1]
        if l == b:
            continue
        elif l != b :
            q.append(l)
    if len(q) == len(set_l):
        cnt += 1
print(cnt)