from wtforms import Form,StringField,PasswordField,SubmitField,RadioField,FieldList,EmailField 
from flask_wtf import FlaskForm

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    apellido = StringField('Apellido')
    email = EmailField('Correo')
    