x = int(input("Enter x "))
fib = 1
i = 1
j = 1
result = 1
while fib <= x:
    j = fib
    fib += i
    i, j = j, i
    result += 1
if i != x:
    result = -1
print(result)
    