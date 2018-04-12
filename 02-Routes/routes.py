from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	return "Estoy en el index..."

@app.route("/saludo")
def saludo():
	return "Hola mundo!!!"

@app.route("/params")
def params():
	param = request.args.get('param1','default param')
	return "El parametro es {}".format(param) 

@app.route("/twoparams")
def params2():
	param = request.args.get('param1','default param')
	param2= request.args.get('param2','default param2')
	return "El parametro es {} , {}".format(param,param2) 

app.run()
#port = 5001, debug = True 