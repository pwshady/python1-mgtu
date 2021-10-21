string = input("Enter string ")
resultString = ""
for i in range(0, len(string)):
    if string[i] == "1":
        resultString += "one"
    else:
        resultString += string[i]
print(resultString)    