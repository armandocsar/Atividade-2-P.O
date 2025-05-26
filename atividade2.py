class Vendedor:
   def __init__(self, nome, nome2):
     self.nome = nome
     self.nome2 = nome2
   
   def informacaoSaida(self):
      print(f"Olá,nome é ", self.nome,"e eu tenho" )

vendedor1 = Vendedor(input('Nome 1 '),input('Sobrenome 2 '))
vendedor2 = Vendedor(input('Nome 2 '),None)

vendedor1.informacaoSaida()
vendedor2.informacaoSaida()
