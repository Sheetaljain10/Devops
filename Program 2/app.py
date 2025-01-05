# app.py
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT)')
    conn.execute('INSERT INTO data (name) VALUES ("Docker Networking Test")')
    conn.commit()
    cursor = conn.execute('SELECT * FROM data')
    data = cursor.fetchall()
    conn.close()
    return f"Database Content: {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
