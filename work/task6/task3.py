lst = [int(s) for s in input().split()]
for i in range(0,int(len(lst)/2)):
    lst[2*i],lst[2*i+1] = lst[2*i+1],lst[2*i]
    print(lst[2*i],lst[2*i+1], end=" ")
if len(lst)%2 ==1:
    print(lst[len(lst)-1])