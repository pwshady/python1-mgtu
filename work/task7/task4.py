num = input()
words = {}
for i in range(0,int(num)):
    lst = [str(s) for s in input().split()]
    for j in range(0,len(lst)):
        if lst[j] in words:
            words[lst[j]] += 1
        else:
            words[lst[j]] = 1
str_ = ""
max_ = 0
for key in sorted(words):
    if words[key] > max_:
        max_ = words[key]
        str_ = key
print(str_)

                   