x = int(input("Enter x "))
li = [x];
j = 1
while x != 0:
    x = int(input("Enter x "))
    li.append(x)
    j += 1
result = 0
if j >= 2:
    for i in range(0,j-1):
        if int(li[i]) < int(li[i+1]):
            result += 1
    print(result)
else:
    print("Error")