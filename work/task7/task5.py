num = input()
words = {}
for i in range(0,int(num)):
    lst = [str(s) for s in input().split()]
    words[lst[0]] = lst[1:]
print(words)
num = input()
for i in range(0,int(num)):
    lst = [str(s) for s in input().split()]
    if lst[1] in words:
        if lst[0] == "write":
            if "W" in words[lst[1]]:
                print("OK")
            else:
                print("Denied")
        elif lst[0] == "read":
            if "R" in words[lst[1]]:
                print("OK")
            else:
                print("Denied")
        elif lst[0] == "execute":
            if "X" in words[lst[1]]:
                print("OK")
            else:
                print("Denied")
        else:
            print("Methot not found")
    else:
        print("File no found")
            
