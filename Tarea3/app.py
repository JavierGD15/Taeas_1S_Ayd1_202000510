from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hola_mundo():
    return '202000510 ANALISIS Y DISEÑO DE SISTEMAS 1 Sección B Bryan Páez'

if __name__ == '__main__':
    app.run()