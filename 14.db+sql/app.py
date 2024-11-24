import sqlite3

connection = sqlite3.connect("november.db") # Create if no exits

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY, 
    name TEXT,
    age INTEGER,
    email TEXT 
)
"""
)
connection.commit()

cursor.execute("""
INSERT INTO Users (id, name, age, email)
VALUES (1, 'Dor', 27, 'dor@gmail.com')
""")
connection.commit()

# Fetch Data 
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fetch Specific Data 
# cursor.execute("SELECT name FROM Users WHERE age > 20")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

cursor.execute("""
UPDATE Users
SET age = 28
WHERE name = 'Dor'
""")
connection.commit()

# Fetch Data 
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Delete 
cursor.execute("""
DELETE FROM Users
WHERE name = 'Dor'
""")
connection.commit()

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
for row in rows:
    print(row)