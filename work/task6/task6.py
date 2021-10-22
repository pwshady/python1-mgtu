lst1 = [int(s) for s in input().split()]
lst2 = [int(s) for s in input().split()]
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
        if lst1[i] == lst2[j]:
            print(lst1[i], end = " ")
