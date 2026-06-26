# RPG
# Nome: Kingdoms of Bondair's
# Versão: 1.00
# Criado e Desenvolvido por Filipe Cavinato

from classes.items import Equipamento, Pocao, Gema, Tomo
from classes.magias import Magias
from classes.personagens import Barbaro, Mago, Orc, Clerigo
from random import choice

pocoes = [['Poção de Vida Pequena', 'Vida', 200],
          ['Poção de Vida Media', 'Vida', 400],
          ['Poção de Vida Grande', 'Vida', 800],
          ['Poção de Força', 'Força', 200],
          ['Poção de Força Maior', 'Força', 400],
          ['Poção de Reinf', 'Força', 850]]

gemas = [['Gema da Vida', 'Vida'],
         ['Gema de Mana', 'Mana']]

tomos = [['Princípios da Magia', 'Magia', 300],
         ['Magia Avançada Vol. 1', 'Magia', 600],
         ['Magia Ancestral [De Elwrin W.]', 'Magia', 1200]]

equipamentos = [['Atordoador de Olrein', 'Machado', 200],
                ['Machado de Aço', 'Machado', 125],
                ['Machado dos Ossos de Tyr', 'Machado', 325],
                ['Espada Antiga', 'Espada', 50],
                ['Espada Ancestral', 'Espada', 150],
                ['Espada Superior', 'Espada', 250],
                ['Espada de Antegemon', 'Espada', 450]]


def main():
    print('Teste Codigo Principal')
    p1 = Barbaro('Kolc')
    p2 = Orc('Heignar')

    print('Testes Manuais:\n')
    print(f'Nome = {p1.nome}')
    print(f'Classe = {type(p1).__name__}')
    print(f'Força = {p1.forca}')
    print(f'Vida = {p1.vida}')

    print(f'\nNome = {p2.nome}')
    print(f'Classe = {type(p2).__name__}')
    print(f'Força = {p2.forca}')
    print(f'Vida = {p2.vida}')

    p1.atacar(p2)
    print(f'\n{p2.nome}: Vida = {p2.vida}')
    p2.atacar(p1)
    print(f'{p1.nome}: Vida = {p1.vida}')

    print('\nUsando Poções:')
    sorteia_pocao = choice(pocoes)
    pocao_vida = Pocao(sorteia_pocao[0], sorteia_pocao[1], sorteia_pocao[2])
    p1.usar_item(pocao_vida)
    escolhe_equipamentos = choice(equipamentos)
    arma = Equipamento(escolhe_equipamentos[0], escolhe_equipamentos[1], escolhe_equipamentos[2])
    p1.usar_item(arma)
    escolhe_tomo = choice(tomos)
    tomo = Tomo(escolhe_tomo[0], escolhe_tomo[1], escolhe_tomo[2])
    p1.usar_item(tomo)

    print('\nTestes Manuais Poções:')
    print(f'Nome = {p1.nome}')
    print(f'Classe = {type(p1).__name__}')
    print(f'Lvl {p1.nivel} ({500 - p1.xp} XP para Lvl {p1.nivel + 1})')
    print(f'XP = {p1.xp} XP')
    print(f'Força = {p1.forca}')
    print(f'Vida = {p1.vida}')

    magia1 = Magias('Bola de Fogo Elemental', 'Ataque', 500)
    p1.usar_magia(magia1, p2)

    print('\nTestes Manuais Magias')
    print(f'Nome = {p2.nome}')
    print(f'Classe = {type(p2).__name__}')
    print(f'Lvl {p2.nivel} ({500 - p2.xp} XP para Lvl {p2.nivel + 1})')
    print(f'XP = {p2.xp} XP')
    print(f'Força = {p2.forca}')
    print(f'Vida = {p2.vida}')

if __name__ == '__main__':
    main()
