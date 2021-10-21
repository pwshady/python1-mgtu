x = int(input("Enter x "))
y = int(input("Enter y "))
if x % 2 == 0:
    if y % 2 == 1:
        print("White")
    else:
        print("Black")
else:
    if y % 2 == 0:
        print("White")
    else:
        print("Black")