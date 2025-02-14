from flask import Flask, render_template,request
import forms


app = Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS805"
    lista=['Juan','Pedro','Mario']
    return render_template("index.html",titulo=titulo,lista=lista);

@app.route('/alumnos',methods=['GET','POST'])
def alumnos():
    nom=''
    ape=''
    edad=0
    email=''
    alumno_clase=forms.UserForm(request.form)
    if request.method == 'post':
        mat=alumno_clase.matricula.data
        ape=alumno_clase.apellido.data
        nom=alumno_clase.nombre.data
        email=alumno_clase.email.data
        print('nombre: {}'.format(nom))
    return render_template("Alumnos.html",form=alumno_clase)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route('/hola')
def hola():
    return 'Hola Mundo x2!'

@app.route('/user/<string:user>')
def user(user):
    return f'Hello {user}!'

@app.route('/numero/<int:n>')
def numero(n):
    return f'El numero es: {n} !' 

@app.route('/user/<int:id>/<string:username>')
def username(id,username):
    return f'el usuario {username} tiene id {id}'

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return f'la suma de {n1} y {n2} es {n1+n2}'

@app.route('/default/')
@app.route('/default/<string:tem>')
def default(tem='Juan'):
    return f'Hola {tem}'

@app.route("/form1")
def form1():
    return '''
    <form action="/form1" method="post">
    <label for="nombre">nombre:</label><br>
    <input type="text"><br>
    </form>
    '''
    
class ticket:
    def __init__(self):
        self.nombreDuenioTicket = ""
        self.cantPersonas = 0
        self.totalBoletos = 0
        self.totalAPagarTicket = 0.0
        self.porcentajeDescuentoTotal = 0.0
        self.metodoPago = ""

    def calcularPago(boletos, metodoPago):
        porcentajeDescuentoTotal = 0.0
        if boletos >= 6:
            porcentajeDescuentoTotal += 0.15
        elif boletos >= 3:
            porcentajeDescuentoTotal += 0.10      

        totalAPagar = (boletos * 12.00) * (1 - porcentajeDescuentoTotal)

        # descuento para la tarjeta del cine(sunpongo) 
        if metodoPago == "si":
            totalAPagar *= 0.9

        return totalAPagar
    
@app.route("/cinepolis", methods=['GET', 'POST'])
def cinepolis():
    totalApagar = 0.0
    error = None
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            cantCom = int(request.form['cantidadCom'])
            tarjeta = request.form.get('tarjeta')
            boletos = int(request.form['cantidadBol'])
            
            if boletos > 7 * cantCom:
                error = "no puedes comprar mas de 7 boletos por persona"
            else:
                totalApagar = ticket.calcularPago(boletos, tarjeta)
            
        except ValueError:
            error = "error, ingresa datos validos"
    return render_template("cinepolis.html",totalApagar=totalApagar,error=error)

# @app.route("/OperasBas")
# def operas():
#     return render_template("OperasBas.html")


@app.route('/OperasBas', methods=['GET', 'POST'])
def operas():
    resultado = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['n1'])
            num2 = float(request.form['n2'])
            operacion = request.form.get('operacion')

            if operacion == 'suma':
                resultado = num1 + num2
            elif operacion == 'resta':
                resultado = num1 - num2
            elif operacion == 'multiplicacion':
                resultado = num1 * num2
            elif operacion == 'division':
                if num2 == 0:
                    resultado = 'no se puede dividir entre cero XD'
                else:
                    resultado = num1 / num2

        except ValueError:
            resultado = "ingresa numeros validos"

    return render_template("OperasBas.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True,port=3000)