import sqlite3

db = sqlite3.connect("guid.db")
cursor = db.cursor()

def add_record():
    name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone = input("Телефон: ")
    guid = [(name, last_name, phone)]

    try:
        cursor.executemany('INSERT INTO guid VALUES(NULL,?,?,?)', guid)
        print("Данные успешно внесены\n")
        db.commit()
    except:
        print('Данные уже есть')