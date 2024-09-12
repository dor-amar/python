import sqlite3

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               task TEXT,
               status TEXT
               )
               ''')

cursor.execute('''
INSERT INTO tasks (task, status)
               VALUES ('Clean','Completed')
               ''')

conn.commit()

cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()

print("To Do List: ")
for task in tasks:
    print(task)

cursor.execute('''
UPDATE tasks
SET status = 'Completed'
WHERE task = 'Buy milk'  
               ''')

cursor.execute('''
DELETE FROM tasks WHERE status = 'Completed'
               ''')

conn.commit()

cursor.execute('SELECT * FROM tasks')
tasks = cursor.fetchall()
print("Remaning Tasks: ")
for task in tasks:
    print(task)

conn.close()