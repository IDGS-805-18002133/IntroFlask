from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World! holas'

@app.route('/hola')
def hola():
    return 'Hola Mundo x2!'

if __name__ == '__main__':
    app.run(debug=True,port=3000)