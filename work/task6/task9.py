str_ = input("Enter sring ")
str1 = str_[0:int((len(str_)+1)/2)]
str2 = str_[int((len(str_)+1)/2):]
print(str2+str1)