x = int(input("Enter x "))
i = 1
if x >= 2 :
    while 2**i < x:
        i += 1
    i -= 1   
    print(str(i) + " " + str(2**i))
else:
    print("Error")
        