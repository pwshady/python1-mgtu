import sys

name = input("Enter file name: ")
date =[]
try:
    file = open(name,'r', encoding='utf-8')
    count = int(file.readline())
    for i in range(count):
        date.append(file.readline())
    print(date)
except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])
    if e.args[0] == 2:
        print("Файл не найден")
    elif e.args[0] == "invalid literal for int() with base 10: ''":
        print("Не верный формат файла")
    