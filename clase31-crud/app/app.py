from flask import Flask,render_template, request, redirect
from dataUser import *
from controller_db import *

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
    productos = obtener_productos()
    titulo = "Tienda CaC"
    return render_template("tienda.html", title=titulo, productos=productos)

# insert
# 1) cargar el form
@app.route("/tienda/cargar_producto")
def insertTienda():
    title = "Nuevo Producto"
    return render_template("form_nuevo_producto.html", title=title)
# 2) enviar los datos del form, por POST

@app.route("/tienda/guardar_nuevo_producto", methods = ['POST'] )
def newProd_Tienda():
    # print(request.form['nombre'])
    nombre_prod = request.form['nombre']
    desc_prod = request.form['descripcion']
    precio_prod = request.form['precio']
    cargar_nuevo_producto(nombre_prod, desc_prod, precio_prod)
    return redirect("/tienda")
    
# update
@app.route("/tienda/editar_producto/<int:id>")
def editar_prod(id):
    title = "Editar Producto"
    prod_por_id = obtener_prod_por_id(id)
    # print(prod_por_id)
    return render_template("form_editar_producto.html", title=title, producto=prod_por_id)

@app.route("/tienda/update_producto", methods=['POST'])
def update_prod():
    id_edit = request.form['id']
    nombre_edit = request.form['nombre']
    desc_edit = request.form['descripcion']
    precio_edit = request.form['precio']
    resp = actualizar_prod(nombre_edit,desc_edit,precio_edit,id_edit)
    return redirect("/tienda")
    # return render_template("tienda.html", resp=resp)

# delete
@app.route('/tienda/borrar_producto/<int:id>')
def delete_prod(id):
    eliminar_prod(id)
    return redirect("/tienda")
    