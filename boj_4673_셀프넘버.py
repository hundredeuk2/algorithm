def self_num(num):
    next_num = num
    
    for i in range(len(str(num))):
        next_num += int(str(num)[i])
    return next_num
    
total_num = set(range(1,10001))
gene_num = set()

for i in range(1, 10001):
    gene_num.add(self_num(i))

self_num = sorted(total_num - gene_num)
for i in self_num:
    print(i)