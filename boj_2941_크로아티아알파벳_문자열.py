word = str(input())
dic = {"c=":"a","c-":"b","dz=":"c","d-":"d","lj":"e","nj":"f","s=":"g","z=":"h"}

for key in dic.keys():
    word = word.replace(key, dic[key])
print(len(word))