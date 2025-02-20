from wtforms import Form,StringField,IntegerField,PasswordField,SubmitField,RadioField,FieldList,EmailField,validators
from flask_wtf import FlaskForm


class UserForm(Form):
    matricula = StringField('Matricula',[
        validators.DataRequired(message='La matricula es requerida'),
        validators.length(min=3, max=8, message='la matricula debe ser de entre 3 y 8 digitos')
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido')
        ])
    apellido = StringField('Apellido',[
        validators.DataRequired(message='El apellido es requerido')
            ])
    email = EmailField('Correo',[
        validators.Email(message='Ingrese un correo valido'),
    ])
    
class ZoodiacForm(Form):
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El nombre es requerido')
        ])
    apellidoPaterno = StringField('Apellido Paterno',[
        validators.DataRequired(message='El apellido es requerido')
            ])
    apellidoMaterno = StringField('Apellido Materno',[
        validators.DataRequired(message='El apellido es requerido')
            ])
    dia = IntegerField('Dia',[
        validators.DataRequired(message='El dia es requerido'),
        validators.NumberRange(min=1,max=31,message='El dia debe ser de 1 a 31')
            ])
    mes = IntegerField('Mes',[
        validators.DataRequired(message='El mes es requerido'),
        validators.NumberRange(min=1,max=12,message='El mes debe ser de 1 a 12')
            ])
    anio = IntegerField('Anio',[
        validators.DataRequired(message='El anio es requerido'),
        validators.NumberRange(min=1900,max=2024,message='El anio debe ser de 1900 a 2024')
            ])
    sexo = RadioField('Sexo',choices=[('M','Masculino'),('F','Femenino')])
    