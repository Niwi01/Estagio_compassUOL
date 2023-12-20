class Lampada:

    def __init__(self, ligada):
        self.ligada = True

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada

lamp = Lampada(False)

lamp.liga()
print(lamp.esta_ligada())

lamp.desliga()
print(lamp.esta_ligada())
