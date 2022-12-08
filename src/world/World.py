from Player import *
from Stadium import *
from Pokemao import *
from Utils import *
# from .Pokemao import definitionPokemao
import os


class colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;96m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;0m"
    BLACK = "\033[90m"


def colorPokemao(namePokemao):
    if namePokemao == PokemaoNames.CHARMAODER.value:
        return colors.RED
    if namePokemao == PokemaoNames.MAOJADINHA.value:
        return colors.BLUE
    if namePokemao == PokemaoNames.MAOSAURO.value:
        return colors.GREEN
    if namePokemao == PokemaoNames.CURSEDHAND.value:
        return colors.BLACK


initializeWorld()
playerName = getPlayerName()
msgInitialWorld()
startHistory(Pokemao,Player,playerName,startPokemaos)


# colorInitialPokemao = colorPokemao(player.pokemaos.name.value)
# print(f"Mestre pokemão {player.name}, seu pokemão inicial é: " +
#       f"{colorInitialPokemao} {player.pokemaos.name.value}")

Pokemao1 = Pokemao(Types.FIRE,PokemaoNames.CHARMAODER,0,0)
Pokemao2 = Pokemao(Types.WATER,PokemaoNames.MAOJADINHA,0,0)
Pokemao3 = Pokemao(Types.WIND,PokemaoNames.MAOSAURO,0,0)
Pokemao4 = Pokemao(Types.DARKNESS,PokemaoNames.CURSEDHAND,0,0)

player2 = Player("player2", Pokemao1)
player2.pokemaos = Pokemao2
print(player2.name,player2.pokemaos.name.value)





