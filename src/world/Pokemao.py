import random
from enum import Enum
class PokemaoNamesAndTypes(Enum):
    CHARMAODER = "FIRE"
    MAOSAURO = "WIND"
    MAOJADINHA = "WATER"
    CURSEDHAND = "DARKNESS"


class colorsOfPokemaos:
    RED = "\033[1;31m"
    BLUE = "\033[1;96m"
    GREEN = "\033[1;32m"
    WHITE = "\033[1;0m"
    BLACK = "\033[90m"




class Pokemao:

    def __init__(self, pokemaoNameAndtype, level, experience):
        self.name = pokemaoNameAndtype.name
        self.type = pokemaoNameAndtype.value
        self.level = level
        self.experience = experience
        self.colorPokemao(pokemaoNameAndtype.name)


    def colorPokemao(self,namePokemao):
        if namePokemao == PokemaoNamesAndTypes.CHARMAODER.name:
            self.color = colorsOfPokemaos.RED
        if namePokemao == PokemaoNamesAndTypes.MAOJADINHA.name:
            self.color = colorsOfPokemaos.BLUE
        if namePokemao == PokemaoNamesAndTypes.MAOSAURO.name:
            self.color = colorsOfPokemaos.GREEN
        if namePokemao == PokemaoNamesAndTypes.CURSEDHAND.name:
            self.color = colorsOfPokemaos.BLACK

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def definitionPokemao(pokemaos):
        pokemaoSorted = random.choice(pokemaos)
        return pokemaoSorted

def initialPokemaos():
    arr = []
    charmaoder = Pokemao(PokemaoNamesAndTypes.CHARMAODER, 0, 0)
    maosauro = Pokemao(PokemaoNamesAndTypes.MAOSAURO, 0, 0)
    maojadinha = Pokemao(PokemaoNamesAndTypes.MAOJADINHA, 0, 0)
    arr.append([charmaoder])
    arr.append(maosauro)
    arr.append(maojadinha)
    return arr