num = input()
words = {}
for i in range(0,int(num)):
    lst1 = [str(s) for s in input().split()]
    if lst1[0] in words:
        words[lst1[0]] += int(lst1[1])
    else:
        words[lst1[0]] = int(lst1[1])
for key in sorted(words):
    print(key, words[key])
    