from Player import *
from Pokemao import *
from Utils import *



# Initializing world
initializeWorld()
# Get name of Player
playerName = getNameOfPlayer()
# Storytelling
infoInitialPokemons()
# Instantiate player with sorted pokemão
intialStoryWithFirstPokemon(playerName, initialPokemaos, Pokemao, Player)
# Clear screen
clearTerminal()


