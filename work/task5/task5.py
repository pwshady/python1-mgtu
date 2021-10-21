x = int(input("Enter x "))
i = 1
li =[]
while i*i < x:
    li.append(i)
    i += 1
for j in range(0,i):
    print(str(j*j) + " ",end="")