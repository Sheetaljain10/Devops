from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/quiet-falcon-21', methods=['GET'])
def quiet_falcon():
    return jsonify({"status": "Ready for requests"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
