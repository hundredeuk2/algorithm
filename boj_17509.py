l = []
for i in range(11):
    l.append(list(map(int, input().split())))
l.sort()

sumnation = 0
penalty = 0
for i in range(11):
    penalty += sumnation + l[i][0] + (20*l[i][1])
    sumnation += l[i][0]

print(penalty)