str_ = input("Enter sring ")
h1 = 0
h2 = 0
for i in range(0,len(str_)):
    if str_[i] == "h":
        h1 = i
        break
for i in range(0,len(str_)):
    if str_[-i] == "h":
        h2 = -i+1
        break
print(str_[0:h1] + str_[h2:])
