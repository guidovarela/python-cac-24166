
"""
DOS
cd 
cd..
dir
dir/w
"""

# comentario linea
"""
comentario 
multilinea
"""

# print("Hola Mundo!")

# variables
nombre = "Guido" #str
numeric = 12 #int
flotante = 12.4 #float
booleans = False #bool

# f"cadena {variable}"

# print("Hola, mi nombre es "+nombre+" y tengo "+str(numeric)+" años")
# print("Hola, mi nombre es",nombre,"y tengo",numeric,"años")

"""
input() -> str
    str(dato) / int() / float() / bool() 
"""
# funciones
"""
def nombre():
    scope / instrucciones
"""
def dataUser():
    user=input("Inserte su nombre")
    edad=int(input("Inserte su edad"))
    print(f"Hola, soy {user} y tengo {edad} años")
    print("salida de la funcion")
    
def saludo(name):
    print(f"hola {name}")

# print(edad + 20)

#condicionales
"""
if (condicion):
    #verdadero
esle:
    #falso
 """
estado = False
def preguntarEstado():
    nombre = "Elvis"
    if estado:
        print(f"{nombre} esta vivo")
    else:
        print(f"{nombre} ha dejado el edificio")

preguntarEstado()

