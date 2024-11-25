import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users'")
if cursor.fetchone() is None:
    for i in range(1, 11):
        cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                       (f"User{i}", f"example{i}@gmail.com", f"{10 * i}", "1000"))

# Удаление пользователя с id=6
# for i in range (1, 2):
#     cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
print('Количество юзеров: ', total_users)

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
sum_balances = cursor.fetchone()[0]
print('Сумма балансов всех юзеров: ', sum_balances)

#Подсчет среднего значения балансов
print('Среднее значение балансов юзеров: ', sum_balances / total_users)
connection.commit()
connection.close()