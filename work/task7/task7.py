num = input()
words = {}
for i in range(0,int(num)):
    lst = [str(s) for s in input().split()]
    for word in lst:
        if word in words:
            words[word] +=1
        else:
            words[word] = 1
sorted_words = {}
sorted_keys = sorted(words, key=words.get, reverse=True)

for w in sorted_keys:
    sorted_words[w] = words[w]
for key in sorted_words:
    print(key, sorted_words[key])
