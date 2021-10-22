lst = [int(s) for s in input().split()]
max_num = min_num = lst[0]
for i in range(0,len(lst)):
    if lst[i] > max_num:
        max_num = lst[i]
        pos_max_num = i
    if lst[i] < min_num:
        min_num = lst[i]
        pos_min_num = i
lst[pos_max_num], lst[pos_min_num] = lst[pos_min_num], lst[pos_max_num]
for i in range(0,len(lst)):
    print(lst[i], end=" ")