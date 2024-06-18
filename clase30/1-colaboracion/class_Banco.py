# from archivo import clase
from class_Cliente import Cliente

class Banco:
   def __init__(self):
       self.cliente1=Cliente("Juan")
       self.cliente2=Cliente("Ana")
       self.cliente3=Cliente("Diego")

   def operar(self):
       self.cliente1.depositar(100)
       self.cliente2.depositar(150)
       self.cliente3.depositar(200)
       self.cliente3.extraer(150)

   def depositos_totales(self):
       total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
       print("El total de dinero en el banco es: {}".format(total))
       self.cliente1.imprimir()
       self.cliente2.imprimir()
       self.cliente3.imprimir()
