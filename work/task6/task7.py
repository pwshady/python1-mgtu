lst1 = [int(s) for s in input().split()]
lst2 = []
for i in range(0,len(lst1)):
    flag = False
    for j in range(0,len(lst2)):
        if lst1[i] == lst2[j]:
            flag = True
    if flag:
        print("ДА")
    else:
        lst2.append(lst1[i])
        print("НЕТ")