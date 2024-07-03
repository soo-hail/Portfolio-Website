from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST' :
        
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        conn = sqlite3.connect('database.db') 
        
        conn.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            ''')
        
        conn.execute('INSERT INTO messages (name, email, message) VALUES (?, ?, ?)', (name, email, message))
        conn.commit()
        conn.close()
    
    return render_template("index.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")