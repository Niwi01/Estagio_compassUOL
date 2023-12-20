class Aviao:
    
    def __init__(self,modelo,velocidade_maxima,cor,capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = 'azul'
        self.capacidade = capacidade
    
lista1 = Aviao('BOIENG456', '1500', '400', 'azul')
lista2 = Aviao('Embraer Praetor 600', '863', '14', 'azul')
lista3 = Aviao('Antonov An-2', '258', '12', 'azul')

print(f'modelo {lista1.modelo}: velocidade máxima {lista1.velocidade_maxima} km/h: capacidade para {lista1.capacidade} passageiros: Cor {lista1.cor}')
print(f'modelo {lista2.modelo}: velocidade máxima {lista2.velocidade_maxima} km/h: capacidade para {lista2.capacidade} passageiros: Cor {lista2.cor}')
print(f'modelo {lista3.modelo}: velocidade máxima {lista3.velocidade_maxima} km/h: capacidade para {lista3.capacidade} passageiros: Cor {lista3.cor}')
