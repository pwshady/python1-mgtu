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
ss = str_[h1+1:h2-1]
ss2 = ""
for i in range(0,len(ss)):
    if ss[i] == "h":
        ss2 += "H"
    else:
        ss2 += ss[i]
print(str_[0:h1+1] + ss2 + str_[h2-1:])