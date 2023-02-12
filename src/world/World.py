from Player import *
from Pokemao import *
from Utils import *


def clearTerminal():
    input("Aperte Enter para continuar")
    os.system("cls||clear")


# Initializing world
initializeWorld()
# Get name of Player
playerName = getNameOfPlayer()
# Storytelling
infoInitialPokemons(clearTerminal)
# Instantiate player with sorted pokemão
player = intialStoryWithFirstPokemon(playerName, initialPokemaos, Pokemao, Player, clearTerminal)
# Open Menu of game
player.openMenu(player.name)
# pokemao2 = Pokemao(PokemaoNamesAndTypes.MAOSAURO, 0,0)
# player.insertPokemao(pokemao2)



# Battle(player, pokemaoRandom)
optionUser = input("Opção: ")
# Open Pokedex
player.pokedex(optionUser)

# for x in "banana":
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
