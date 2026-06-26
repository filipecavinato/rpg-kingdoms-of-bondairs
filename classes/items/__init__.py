# Modulo criado por Filipe Cavinato

from rich import print
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__ (self, nome, tipo, valor):
        self.nome = nome
        self.tipo = tipo
        self.valor = valor

    @abstractmethod
    def usar(self, personagem):
        pass


class Equipamento(Item):
    def __init__ (self, nome, tipo, valor):
        super().__init__(nome, tipo, valor)

    def usar(self, personagem):
        print(f':dagger:  [bold]{personagem.nome}[/] equipou [yellow]{self.nome}[/] (+ {self.valor} de Força)')
        personagem.forca += self.valor


class Pocao(Item):
    def __init__ (self, nome, tipo, valor):
        super().__init__(nome, tipo, valor)

    def usar(self, personagem):
        print(f':test_tube: [bold]{personagem.nome}[/] usou [purple]{self.nome}[/] ', end='')
        if self.tipo.title() == 'Vida':
            print(f'(+ {self.valor} HP)')
            personagem.vida += self.valor
        elif self.tipo.title() == 'Força':
            print(f'(+ {self.valor} de Força)')
            personagem.forca += self.valor


class Gema(Item):
    def __init__ (self, nome, tipo):
        super().__init__(nome, tipo)

    def usar(self, personagem):
        print(f':gem_stone: [bold]{personagem.nome}[/] usou [green]{self.nome}[/]')
        if self.tipo.title() == 'Vida':
            personagem.vida = personagem.vida_maxima
        elif self.tipo.title() == 'Mana':
            personagem.mana = personagem.mana_maxima


class Tomo(Item):
    def __init__ (self, nome, tipo, valor):
        super().__init__(nome, tipo, valor)

    def usar(self, personagem):
        if not personagem.pode_usar_magia:
            if self.nome == 'Princípios da Magia':
                print(f':scroll: {personagem.nome} leu [blue]{self.nome}[/]')
                print(f':bulb: {personagem.nome} [yellow]aprendeu a usar Magia![/]')
                personagem.pode_usar_magia = True
                personagem.mana += self.valor
            else:
                print(f':scroll: :prohibited: [red]O Item não pode ser usado![/]')
        else:
            print(f':scroll: {personagem.nome} usou [blue]{self.nome}[/]')
            if self.tipo.title() == 'Magia':
                personagem.mana += self.valor
