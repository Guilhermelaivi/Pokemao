import random
from enum import Enum

class colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;96m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;0m"
    BLACK = "\033[90m"

class PokemaoNamesAndTypes(Enum):
    CHARMAODER = "FIRE"
    MAOSAURO = "WIND"
    MAOJADINHA = "WATER"
    CURSEDHAND = "DARKNESS"

class Pokemao: 
    def __init__(self,PokemaoNamesAndTypes,level,experience):
        self.name = PokemaoNamesAndTypes.name
        self.type = PokemaoNamesAndTypes.value
        self.level = level
        self.experience = experience
        self.colorPokemao(PokemaoNamesAndTypes.name)

    def colorPokemao(self, namePokemao):
        if namePokemao == PokemaoNamesAndTypes.CHARMAODER.name:
            self.color = colors.RED
        if namePokemao == PokemaoNamesAndTypes.MAOJADINHA.name:
            self.color = colors.BLUE
        if namePokemao == PokemaoNamesAndTypes.MAOSAURO.name:
            self.color = colors.GREEN
        if namePokemao == PokemaoNamesAndTypes.CURSEDHAND.name:
            self.color = colors.BLACK

    def definitionPokemao(arr):
        pokemaoSorted = random.choice(arr)         
        return pokemaoSorted 
    def __str__(self) -> str:
        return str(self.__class__) + ":" + str(self.__dict__)

def startPokemaos():
    arr = []
    charmaoder = Pokemao(PokemaoNamesAndTypes.CHARMAODER,0,0) 
    maosauro = Pokemao(PokemaoNamesAndTypes.MAOSAURO,0,0)
    maojadinha = Pokemao(PokemaoNamesAndTypes.MAOJADINHA,0,0)
    arr.append(charmaoder)
    arr.append(maosauro)
    arr.append(maojadinha)
    return arr




