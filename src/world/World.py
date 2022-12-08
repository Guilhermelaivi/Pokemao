from Player import *
from Stadium import *
from Pokemao import *
from Utils import *
import os

initializeWorld()
playerName = getPlayerName()
msgInitialWorld()
startHistory(Pokemao,Player,playerName,startPokemaos)


# Pokemao1 = Pokemao(Types.FIRE,PokemaoNames.CHARMAODER,0,0)
# Pokemao2 = Pokemao(Types.WATER,PokemaoNames.MAOJADINHA,0,0)
# Pokemao3 = Pokemao(Types.WIND,PokemaoNames.MAOSAURO,0,0)
# Pokemao4 = Pokemao(Types.DARKNESS,PokemaoNames.CURSEDHAND,0,0)

# player2 = Player("player2", Pokemao1)
# player2.pokemaos = Pokemao2
# print(player2.name,player2.pokemaos.name.value)





