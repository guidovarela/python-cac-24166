""""

    Ejemplo: ciclo while
    solicitar 3 números y sumarlos
    
"""

contador = 0
sumatoria = 0

while contador <=3 and sumatoria == 0:
    numero = float(input(f"Ingrese el número {contador}:"))
    sumatoria += numero
    contador += 1
print(f"La suma de {contador} numeros es {sumatoria}")

