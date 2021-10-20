students = int(input("Enter students: "))
apples = int(input("Enter apples: "))
print("apples from students: " + str(int(apples / students)), end="")
print(", apples in a basket: " + str(apples - (int(apples / students)) * students))