num = input()
words = {}
for i in range(0,int(num)):
    lst1 = [str(s) for s in input().split()]
    words[lst1[0]] = lst1[1]
str_ = input()
if str_ in words:
    print(words[str_])
else:
    print("No key")
    