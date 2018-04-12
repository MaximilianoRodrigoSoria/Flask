from flask import Flask
from flask import request
from flask import render_template
import forms 
app = Flask(__name__)

@app.route('/')
def index():	
	return render_template("index.html")

@app.route('/contacto', methods=['GET','POST'])
def contacto():
	comment_form = forms.comentarioForm(request.form)	
	if request.method == 'POST' and comment_form.validate():
		print comment_form.username.data
		print comment_form.comment.data
		print comment_form.email.data
	return render_template("contacto.html", form = comment_form)


if __name__ == '__main__':
	app.run(debug = True, port = 8000)