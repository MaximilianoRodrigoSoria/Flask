from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return "Estoy en el index..."

@app.route("/saludo")
@app.route("/saludo/<nombre>")
@app.route("/saludo/<nombre>/<apellido>")
@app.route("/saludo/<nombre>/<apellido>/<int:edad>")
def saludo(nombre='valor por defecto',apellido='',edad=0):
	return "Hola {}, {}, {}".format(nombre,apellido,edad)





if __name__ == '__main__':
	app.run(debug = True, port = 8000)