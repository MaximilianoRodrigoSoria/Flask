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

@app.route("/params")
def params():
	param = request.args.get('param1','default param')
	return "El parametro es {}".format(param) 

@app.route("/twoparams")
def params2():
	param = request.args.get('param1','default param')
	param2= request.args.get('param2','default param2')
	return "El parametro es {} , {}".format(param,param2) 



if __name__ == '__main__':
	app.run(debug = True, port = 8000)