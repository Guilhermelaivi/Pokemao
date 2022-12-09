import random
from random import randrange
from enum import Enum

class Levels(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    BOSS = "BOSS"

class PokemaoNamesAndTypes(Enum):
    CHARMAODER = "FIRE"
    MAOSAURO = "WIND"
    MAOJADINHA = "WATER"
    CURSEDHAND = "DARKNESS"

class PokemaoNamesAndTypesNPC(Enum):
    MAO2 = "FIRE"
    MAO3 = "WIND"
    MAO4 = "WATER"
    MAO5 = "DARKNESS"
    MAO6 = "DARKNESS"
    MAO7 = "FIRE"



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

    def colorPokemao(self, namePokemao):
        if namePokemao == PokemaoNamesAndTypes.CHARMAODER.name:
            self.color = colorsOfPokemaos.RED
        if namePokemao == PokemaoNamesAndTypes.MAOJADINHA.name:
            self.color = colorsOfPokemaos.BLUE
        if namePokemao == PokemaoNamesAndTypes.MAOSAURO.name:
            self.color = colorsOfPokemaos.GREEN
        if namePokemao == PokemaoNamesAndTypes.CURSEDHAND.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO2.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO3.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO4.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO5.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO6.name:
            self.color = colorsOfPokemaos.BLACK
        if namePokemao == PokemaoNamesAndTypesNPC.MAO7.name:
            self.color = colorsOfPokemaos.BLACK
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def definitionPokemao(pokemaos):
        pokemaoSorted = random.choice(pokemaos)
        return pokemaoSorted





def generateRandomPokemon(category):
    if(category == "LOW"):
        return Pokemao(random.choice(list(PokemaoNamesAndTypesNPC)), random.randint(0, 2), 0)
    if (category == "MEDIUM"):
        return Pokemao(random.choice(list(PokemaoNamesAndTypesNPC)), random.randint(3, 5), 0)
    if (category == "BOSS"):
        return Pokemao(random.choice(list(PokemaoNamesAndTypesNPC)), random.randint(6, 9), 0)
def initialPokemaos():
    arr = []
    charmaoder = Pokemao(PokemaoNamesAndTypes.CHARMAODER, 0, 0)
    maosauro = Pokemao(PokemaoNamesAndTypes.MAOSAURO, 0, 0)
    maojadinha = Pokemao(PokemaoNamesAndTypes.MAOJADINHA, 0, 0)
    cursedhand = Pokemao(PokemaoNamesAndTypes.CURSEDHAND, 0, 0)
    arr.append(charmaoder)
    arr.append(maosauro)
    arr.append(maojadinha)
    arr.append(cursedhand)
    return arr
