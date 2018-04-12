from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():	
	return render_template("index.html")

@app.route('/contacto')
def contacto():	
	return render_template("contacto.html")


if __name__ == '__main__':
	app.run(debug = True, port = 8000)