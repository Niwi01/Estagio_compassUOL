class Pessoa:
    
    def __init__(self,id):
        self.__nome = None
        self.id = id
        
    def nome(self, nome):
        self.__nome = nome
        
    def nome2(self):
        return self.__nome


pessoa = Pessoa(0) 
pessoa.nome2 = 'Fulano De Tal'
print(pessoa.nome2)