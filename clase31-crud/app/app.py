from flask import Flask,render_template

app = Flask(__name__)



# home
@app.route("/")
def hello_world():
    title = "Hola Mundo!"
    # return render_template("plantilla.html",datos)
    return render_template('index.html',titulo=title)

@app.route('/contacto')
def dataContacto():
    title="Contacto"
    return render_template("contacto.html",title=title)

@app.route('/tienda')
def getTienda():
    return render_template("tienda.html")