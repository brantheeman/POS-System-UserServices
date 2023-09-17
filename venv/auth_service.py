from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    return request.json

@app.route('/login', methods=['POST'])
def login():
    return request.json

if __name__ == '__main__':
    app.run()