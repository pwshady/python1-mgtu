x1 = int(input("Enter1 x "))
y1 = int(input("Enter1 y "))
x2 = int(input("Enter2 x "))
y2 = int(input("Enter2 y "))
if x1 % 2 == 0:
    if y1 % 2 == 1:
        cell1 = "White"
    else:
        cell1 = "Black"
else:
    if y1 % 2 == 0:
        cell1 = "White"
    else:
        cell1 = "Black"
        
if x2 % 2 == 0:
    if y2 % 2 == 1:
        cell2 = "White"
    else:
        cell2 = "Black"
else:
    if y2 % 2 == 0:
        cell2 = "White"
    else:
        cell2 = "Black"
        
if cell1 == cell2:
    print("Да")
else:
    print("Нет")
