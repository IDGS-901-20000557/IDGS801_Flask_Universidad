from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('correo')
    
class UserFormMaestro(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidom=StringField('apellidom')
    apellidop=StringField('apellidop')
    email=EmailField('correo')
    