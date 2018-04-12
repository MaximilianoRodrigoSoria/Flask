from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import * 
from wtforms import validators
class comentarioForm(Form):
	username= StringField('Nombre de usuario',
		[validators.length(min=4,max=25,message='Ingrese un nombre de usuario valido!'),
		 validators.Required(message='El nombre de usuario no debe estar vacio')])
	email = EmailField('Correo electronico',
		[validators.Email(message="Ingrese un Email valido!!!")])
	comment = TextField('Comentario')
	