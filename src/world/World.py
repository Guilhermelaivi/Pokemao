from Player import *
from Stadium import *
from Pokemao import *
# from .Pokemao import definitionPokemao
import os


class colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;96m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;0m"


def colorPokemao(namePokemao):
    if namePokemao == PokemaoNames.CHARMAODER.value:
        return colors.RED
    if namePokemao == PokemaoNames.MAOJADINHA.value:
        return colors.BLUE
    if namePokemao == PokemaoNames.MAOSAURO.value:
        return colors.GREEN


print("------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")

playerName = input("Defina seu nome:\n")
os.system("cls||clear")
print("Agora você começará sua jornada no mundo pokemão.\nNote que você já começa com um pokemão e poderá capturar mais ao longo de sua jornada!")
initialPokemao = Pokemao.definitionPokemao()
player = Player(playerName, initialPokemao)
colorInitialPokemao = colorPokemao(player.pokemaos.name.value)
print(f"Mestre pokemão {player.name}, seu pokemão inicial é: " +
      f"{colorInitialPokemao} {player.pokemaos.name.value}")


