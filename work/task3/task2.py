string = input("Enter string ")
for i in range(0, len(string)):
    if string[i] == " ":
        break
print(string[i+1:len(string)] + " " + string[0:i])
##while string[-1] == " ":
##    string = string[0:-1]
##if len(string) > 0:
##    word = 1
##for i in range(0, len(string)):
##    if string[i] == " ":
##        word += 1
##print("Word = " + str(word))
##    