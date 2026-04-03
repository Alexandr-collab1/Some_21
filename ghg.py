import sqlite3


connection = sqlite3.connect('AnimalKingdom.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Animals (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Type TEXT NOT NULL
)
''')

animals_data = [
    ("Лев", "Ссавець"),
    ("Крокодил", "Плазун"),
    ("Орел", "Птах"),
    ("Морська черепаха", "Плазун"),
    ("Мавпа", "Ссавець")
]

cursor.executemany('INSERT INTO Animals (Name, Type) VALUES (?, ?)', animals_data)


cursor.execute('UPDATE Animals SET Name = "Сокіл" WHERE Name = "Орел"')

print("--- Ссавці у базі даних ---")
cursor.execute('SELECT * FROM Animals WHERE Type = "Ссавець"')
mammals = cursor.fetchall()
for animal in mammals:
    print(f"ID: {animal[0]}, Назва: {animal[1]}, Тип: {animal[2]}")


print("\n--- Всі записи у таблиці Animals ---")
cursor.execute('SELECT * FROM Animals')
all_animals = cursor.fetchall()
for animal in all_animals:
    print(f"ID: {animal[0]}, Назва: {animal[1]}, Тип: {animal[2]}")


connection.commit()
connection.close()