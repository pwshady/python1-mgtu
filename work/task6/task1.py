lst = [int(s) for s in input().split()]
for i in range(0,len(lst)):
    if lst[i] % 2 !=0:
        print(lst[i], end=" ")
