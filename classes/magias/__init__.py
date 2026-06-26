# Modulo criado por Filipe Cavinato

class Magias:
    def __init__ (self, nome, tipo, poder):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder

    def ativar(self, alvo):
        if self.tipo.title() == 'Ataque':
            alvo.vida -= self.poder
        elif self.tipo.title() == 'Cura':
            alvo.vida += self.poder
