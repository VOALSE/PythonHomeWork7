# import sqlite3

# def guid():
#     db = sqlite3.connect("guid.db")
#     cursor = db.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS guid
#         (
#         Код INTEGER PRIMARY KEY AUTOINCREMENT,
#         Имя TEXT,
#         Фамилия TEXT,
#         Телефон TEXT
#     )''')

#     # guid=[("Иван", "Азанов", "89631234567"), 
#     #     ("Иван", "Азанов", "89631234567"),
#     #     ("Иван", "Азанов", "89631234567")]

#     # try:
#     #     cursor.executemany('INSERT INTO guid VALUES(NULL,?,?,?)', guid)
#     #     db.commit()
#     # except:
#     #     print('Данные уже есть')

# guid()