from menu import input_chuise
import sqlite3

def guid():
    db = sqlite3.connect("guid.db")
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS guid
        (
        Код INTEGER PRIMARY KEY AUTOINCREMENT,
        Имя TEXT,
        Фамилия TEXT,
        Телефон TEXT
    )''')
guid()
input_chuise()