string = input("Enter string ")
first = -1
second = 0
for i in range(0, len(string)):
    if string[i] == "f":
        if first > -1:
            second = i
        else:
            first = i
if second == 0:
    print(first)
else:
    print(str(first) + " " + str(second))
        
    