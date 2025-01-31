from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo="IDGS805"
    lista=['Juan','Pedro','Mario']
    return render_template("index.html",titulo=titulo,lista=lista);

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

if __name__ == '__main__':
    app.run(debug=True,port=3000)