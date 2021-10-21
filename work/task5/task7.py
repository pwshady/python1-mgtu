x = int(input("Enter x "))
li =[1]
i = 1
li.append(i)
while i <= x:
    result = li[i-1]+li[i]
    li.append(result)
    i += 1
print(li[i-2])