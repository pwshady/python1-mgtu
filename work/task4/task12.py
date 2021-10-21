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
month = int(input("Enter month "))
day = int(input("Enter1 day "))
if year.get(str(month)) == str(day):
    day = 0
    month += 1
day += 1
month = month % 12
print(str(day) + "-" + str(month) + "-2021")