from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à Calculadora Flask!"

if __name__ == '__main__':
    app.run(debug=True)
