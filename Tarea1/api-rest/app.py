from flask import Flask

app = Flask(__name__)

@app.route('/holamundo')
def hello_world():
    return 'Hola mundo!'

@app.route('/nombre')
def nombre():
    return 'Javier Alexander Giron Donis'



if __name__ == '__main__':
    app.run(debug=True)