from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
	saludo = "estas en el index"
	myList=[1,2,3,4]
	return render_template("index.html",nombre=saludo,edad='',myList=myList)

@app.route('/saludo/<nombre>')
def saludo(nombre=""):
	edad=18
	myList=[1,2,3,4]
	return render_template("index.html",nombre=nombre, edad=edad,myList=myList)

@app.route('/saludo2')
def saludo2():
	param = request.args.get('param','param default')
	myList=[1,2,3,4]
	return render_template("index.html",nombre=param, edad='',myList=myList)

if __name__ == '__main__':
	app.run(debug = True, port = 8000)