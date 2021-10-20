class1 = int(input("Enter class1: "))
class2 = int(input("Enter class2: "))
class3 = int(input("Enter class3: "))
table1 = int(class1 / 2)
if class1 > (table1 * 2):
    table1 += 1
table2 = int(class1 / 2)
if class2 > (table2 * 2):
    table1 += 1
table3 = int(class1 / 2)
if class3 > (table3 * 2):
    table1 += 1
print(str(table1 + table2 + table3))