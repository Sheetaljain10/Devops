from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, name TEXT)''')
    conn.commit()
    conn.close()

@app.route('/add', methods=['POST'])
def add_data():
    name = request.json.get('name')
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO data (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Data added!"}), 200

@app.route('/get', methods=['GET'])
def get_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM data')
    data = c.fetchall()
    conn.close()
    return jsonify(data), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
