from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import * 
class comentarioForm(Form):
	username= StringField('Nombre de usuario')
	email = EmailField('Correo electronico')
	comment = TextField('Comentario')
	