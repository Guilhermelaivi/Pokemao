from Player import *
from Stadium import *
from Pokemao import * 
# from .Pokemao import definitionPokemao 
import os

class colors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

def defineInitialColorPokemao(initialPokemao):
    if initialPokemao == "MAOJADINHA":
        return colors.OKGREEN
    elif initialPokemao == "CHARMAODER":
        return colors.HEADER
    return colors.OKCYAN

print("------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")


playerName = input("Defina seu nome:\n")
os.system("cls||clear")

print("Seu nome é:",playerName)
print("Agora você começará sua jornada no mundo pokemão.\nNote que você já começa com um pokemão e poderá capturar mais ao longo de sua jornada!")

initialPokemao = Pokemao.definitionPokemao()

player = Player(playerName,initialPokemao)
colorInitialPokemao = defineInitialColorPokemao(initialPokemao.name.value)
os.system("cls||clear")

print(f"Joador {player.name}, você foi contemplado com o pokemon " + colorInitialPokemao + f"{initialPokemao.name.value}" +  colors.ENDC + " para sua jornada")
input("Aperte Enter para continuar")
os.system("cls||clear")
print("Você precisa de pokemãos, para isso é necessário capturá-los")
print("Ao obter 3 pokemãos, você poderá disputar batalhas em prol de se tornar um líder pokemão")
print(f"Jogador {player.name} você acaba de receber sua pokedex.\n O que você deseja fazer agora?")

