nans = []
for _ in range(9):
    nans.append(int(input()))
nans.sort()

SUM = sum(nans)
for i in range(8):
    for j in range(i+1,9):
        odd = nans[i] + nans[j]
        # print(tmp)
        tmp = SUM-odd
        if tmp == 100:
            break
    if tmp == 100:
        break

nans.pop(j)
nans.pop(i)

for x in nans:
    print(x)