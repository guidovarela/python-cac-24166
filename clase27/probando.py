"""Comentario
 multilinea"""

textos = """Hola, 
esto es un
 texto 
 largo"""

nombre="ANALIA"
nombre2="Analia"
# print(len(nombre))
# print(nombre[0])
# print(nombre > nombre2)

# print(nombre.lower() != nombre2)


# cadena -> lista de caracteres
# ["A","N","A","L","I","A"]
# print(nombre[5])

# Lista -> Matriz
# lista[indice]
numeros = [2,3,4,5,56,43,7,12,45,1,56,"string"]
# print(len(numeros))

dias = ["Lunes", "Martes", "Miércoles"]

# nuevoDia = input("Cargar nuevo dia: ")
# posicionDia = int(input("Numero de posicion del dia"))
# dias.append(nuevoDia)
# dias.insert(posicionDia,nuevoDia)

# for i in range(len(dias)):
#     print(dias[i])

# eliminar
numeros.remove(56)
# print(numeros)

# diccionarios
diccionario = {'Juan': 56, 'Ana': 15, 'Julia': 25, 'Nina':46,}
# print(diccionario["Ana"])

nuevoUser = input("Nombre: ")
edadUser = int(input("Edad: "))
diccionario[nuevoUser]=edadUser
print(diccionario)

# for i in diccionario.keys(): 
#     print(diccionario[i])
# # for key,value in diccionario.items(): 
# #     print(key)
# for key,value in diccionario.items(): 
#     print(value)


