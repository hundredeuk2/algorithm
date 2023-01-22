n = str(input())
word_x = n.lower()

count = []
for i in list(set(word_x)) :
    tmp_count = 0
    for j in range(len(word_x)):
        
        if i == word_x[j]:
            tmp_count += 1
    count.append(tmp_count)
    
if count.count(max(count)) > 1:
    print("?")
else :
    print(list(set(word_x))[count.index(max(count))].upper())