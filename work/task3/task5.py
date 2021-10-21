string = input("Enter string ")
resultString = ""
for i in range(0, len(string)):
    if string[i] == "@":
        resultString += ""
    else:
        resultString += string[i]
print(resultString)    