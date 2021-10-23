num = input()
words = {}
for i in range(0,int(num)):
    lst = [str(s) for s in input().split()]
    words[lst[0]] = lst[1:]
print(words)
num = input()
for i in range(0,int(num)):
    city = input()
    for key in words:
        if city in words[key]:
            print(key)
            break
        