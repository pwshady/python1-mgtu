x = int(input("Enter x "))
i = 2
while i <= x:
    if x % i != 0:
        i += 1
    else:
        print(i)
        break