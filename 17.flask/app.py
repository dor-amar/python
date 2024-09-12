from flask import Flask, render_template, request, redirect
import sqlite3


app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row 
    print("Connected to DB")
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE,
                   email TEXT UNIQUE
                   )
                   ''')
    conn.commit()
    conn.close()
    print("Init DB")

@app.route('/')
def home():
    return "Hello This is my API"


@app.route('/users')
def users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return render_template('users.html',users=rows)


@app.route('/add_user', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()
        return redirect('/users')
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Add User">
        </form>
    '''


if __name__ == '__main__':
    # פעולות הכנה להרים את האפליקציה

    get_db_connection() # Check Connection to DB
    init_db() # Create table

    # להתחיל את האפליקציה
    app.run(port=8080, debug=True)

