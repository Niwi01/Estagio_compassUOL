class Passaro:

    def __init__(self,nome):
        self.nome = nome

class Pato(Passaro):
  
    def __init__(self,nome,som1):
      super().__init__(nome)
      self.som1 = som1
      

class Pardal(Passaro):
  
    def __init__(self,nome,som2):
      super().__init__(nome)
      self.som2 = som2
 



pato = Pato('Pato', 'Quack Quack')
pardal = Pardal('Pardal', 'Piu Piu')

print(pato.nome)
print('Voando...')
print(f'{pato.nome} emitindo som...')
print(pato.som1)
print(pardal.nome)
print('Voando...')
print(f'{pardal.nome} emitindo som...')
print(pardal.som2)