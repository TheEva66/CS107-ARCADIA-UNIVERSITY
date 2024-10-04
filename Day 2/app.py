#runs a specified html file
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('.', 'Greg.html'), 200

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')