from Player import *
from Stadium import *
from Pokemao import * 
# from .Pokemao import definitionPokemao 
import os

print("------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")


player = input("Defina seu nome:\n")
os.system("cls||clear")

print("Seu nome é:",player)
print("Agora você começará sua jornada no mundo pokemão.\nNote que você já começa com um pokemão e poderá capturar mais ao longo de sua jornada!")

initialPokemao = Pokemao.definitionPokemao()
print(initialPokemao.name)