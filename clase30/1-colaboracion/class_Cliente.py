class Cliente:
   def __init__(self,nombre):
       self.nombre=nombre
       self.monto=0

   def depositar(self,monto):
       self.monto=self.monto+monto

   def extraer(self,monto):
       self.monto=self.monto-monto

   def retornar_monto(self):
       return self.monto

   def imprimir(self):
       print("{} tiene depositada la suma de {}".format(self.nombre,self.monto))

       

