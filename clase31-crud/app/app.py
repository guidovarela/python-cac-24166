from flask import Flask,render_template
from dataUser import *
from controlller_db import conexionMySQL

app = Flask(__name__)

# home
@app.route("/")
def dataHome():
    title = "Hola Mundo!"
    # return render_template("plantilla.html",datos)
    return render_template('index.html',titulo=title,users=users)

@app.route("/persona/<int:id>")
def dataUsers(id):
    title="Staff"
    return render_template("persona.html",title=title,user=users[id])

@app.route('/contacto')
def dataContacto():
    title="Contacto"
    return render_template("contacto.html",title=title)

@app.route('/tienda')
def getTienda():
    conexion = conexionMySQL()
    titulo = "Tienda CaC"
    return render_template("tienda.html", title=titulo, conexion=conexion)