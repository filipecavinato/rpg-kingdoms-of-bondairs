# Modulo criado por Filipe Cavinato

from rich import print
from abc import ABC
from random import randint, choice
from math import pow

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.forca = None
        self.mana = None
        self.mana_maxima = None
        self.vida = 1000
        self.vida_maxima = self.vida
        self.pode_usar_magia = False
        self.xp = 0
        self.nivel = 0
        pass

    def atacar(self, alvo):
        alvo.vida -= self.forca
        self.ganhar_experiencia(alvo)

    def usar_item(self, item):
        item.usar(self)

    def ganhar_experiencia(self, alvo):
        self.xp += round(pow(alvo.forca, 0.5) * 2.5)
        print(f' {self.nome} ganhou {self.xp} XP')

        if self.xp == 500:
            self.nivel += 1
            self.xp = 0
            print(f':up!_button: [yellow]{self.nome} subiu de nível! Lvl {self.nivel}[/]')
        elif self.xp > 500:
            resultado = self.xp // 500
            self.nivel += resultado
            self.xp -= (resultado * 500)
            print(f':up!_button: [yellow]{self.nome} subiu de nível! Lvl {self.nivel}[/]')

    def usar_magia(self, magia, alvo):
        if self.pode_usar_magia:
            print(f':crystal_ball: [bold]{self.nome}[/] usou [green]{magia.nome}[/] em [red]{alvo.nome}[/]')
            magia.ativar(alvo)
        else:
            print(f':prohibited: [red]{self.nome} não possui habilidade de Magia[/]')


class Barbaro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = randint(100, 400)
        self.mana = 0


class Clerigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = randint(50, 200)
        self.pode_usar_magia = True
        self.mana = 500


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = randint(100, 250)
        self.pode_usar_magia = True
        self.mana = 1000


class Orc(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.forca = randint(400, 800)
