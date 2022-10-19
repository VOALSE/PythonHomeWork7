import sqlite3

db = sqlite3.connect("guid.db")
cursor = db.cursor()

def previev_baza():
    for i in  cursor.execute('SELECT * FROM guid'):
        print(*i)
    print()