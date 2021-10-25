import re

data_books = []

def shadow_accounting(num, price):
    if num * price < 500:
        return num * price + 100
    else:
        return num * price
    

def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        strings = file.readlines()
        strings = str(strings)
        strings = strings.replace(r"\n', '", ' ')
        strings = strings[2:-2]
        restrings = strings[::-1]
        reindexs = re.findall(r".-...-.....-.-...",restrings)
        rebooks = []
        data_books = []
        for reindex in reindexs:
            pos = restrings.find(reindex)
            rebooks.append(restrings[0:pos+17])
            restrings = restrings[pos+18:]
        for book in rebooks:
            data_books.append(book[::-1].split("|"))
    return data_books

def get_books(db, find_text):
    find_books = []
    for book in db:
        pos = book[1].lower().find(find_text)
        if pos >= 0:
            find_books.append(book)
    return find_books

def get_totals(db):
    totals = []
    for book in db:
        totals.append((book[0],shadow_accounting(int(book[3]), float(book[4]))))
    return totals
            
            
data_books = read_file("books.csv")
#print(get_books(data_books, "python"))
print(get_totals(data_books))