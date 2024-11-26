from flask import Flask, render_template, request, redirect
import sqlite3
import re

app = Flask(__name__)

# Define Functions for The app 
def email_validation(email):
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    return valid


def get_db_connection():
    with sqlite3.connect("november.db") as conn:
      conn.row_factory = sqlite3.Row
      print("Connected to the DB")
    return conn

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                       id INTEGER PRIMARY KEY,
                       name TEXT,
                       email TEXT
                       )
            """)
        conn.commit()
    print("Init DB")

# Define Routes 
@app.route('/')
def home():
    return "Welcome to my API"

@app.route('/users')
def users():
    # Fetch data from db on all users and display 
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
    return render_template('users.html',users = rows)
            

@app.route('/add_users', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        if email_validation:
            email = request.form['email']
        else:
            print("Enter a Vaild mail")
        name = request.form['name']

        with get_db_connection() as conn:
          cursor = conn.cursor()
          cursor.execute('INSERT INTO users (name,email) VALUES (?,?)',(name,email))
          conn.commit()
          return redirect('/users') 
    return '''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Add User">
        </form>
    '''

# Run The application
if __name__ == '__main__':
    # Init the DB Or Connect to the DB 
    init_db()

    # Run the App
    app.run(port=8080,debug=True)
