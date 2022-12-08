from Categories import Types
from Categories import PokemaoNames
import random

class Pokemao: 
    def __init__(self,type,name,level,experience):
        self.name = name
        self.type = type
        self.level = level
        self.experience = experience
    def definitionPokemao():
        pokemaoSorted = random.choice(arr)         
        return pokemaoSorted 

def startPokemaos():
    arr = []
    charmaoder = Pokemao(Types.FIRE,PokemaoNames.CHARMAODER,0,0) 
    maosauro = Pokemao(Types.WIND,PokemaoNames.MAOSAURO,0,0)
    maojadinha = Pokemao(Types.WATER,PokemaoNames.MAOJADINHA,0,0)
    arr.append(charmaoder)
    arr.append(maosauro)
    arr.append(maojadinha)
    return arr



