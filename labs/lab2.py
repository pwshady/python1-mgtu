import random

year = {
    "1": "31",
    "2": "28",
    "3": "31",
    "4": "30",
    "5": "31",
    "6": "30",
    "7": "31",
    "8": "31",
    "9": "30",
    "10": "31",
    "11": "30",
    "12": "31"
    }

def get_day(piple):
    dete_best_day = []
    for i in range(piple):
        month = random.randint(1,12)
        max_day = int(year.get(str(month)))
        day = random.randint(1,max_day)
        dete_best_day.append([month,day])
    return unic_element(dete_best_day)

#Проверка уникальности элементов
def unic_element(arr_element):
    for i in range(len(arr_element)-1):
        for j in range(i+1, len(arr_element)):
            if arr_element[i] == arr_element[j]:
                return True
    return False

def birthday(n, piple):
    luck = 0
    for i in range(n):
        if get_day(piple):
            luck += 1
    return luck/n

print(birthday(10000,60))
