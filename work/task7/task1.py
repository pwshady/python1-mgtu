lst1 = [str(s) for s in input().split()]
words = {}
for i in range(0,len(lst1)):
    if lst1[i] in words:
        print(words[lst1[i]], end = " ")
        words[lst1[i]] += 1
    else:
        print(0, end = " ")
        words[lst1[i]] = 1
##for i in range(0,len(words)):
##    print(words)