num = int(input("Enter num: "))
if (num - int(num / 100) * 100) == 1:
    num += 99
print(str(int(num / 100)))