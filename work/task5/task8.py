x = int(input("Enter x "))
li = [x];
j = 1
while x != 0:
    x = int(input("Enter x "))
    li.append(x)
    j += 1
result = 0
tec_result = 0 
if j >= 2:
    for i in range(0,j-1):
        if int(li[i]) == int(li[i+1]):
            if tec_result == 0:
                tec_result += 1
            tec_result += 1
        else:
            if tec_result > result:
                result = tec_result
                tec_result = 0
print(result)