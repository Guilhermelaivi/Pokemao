import os

class TextColors:
    ENDC = "\033[0m" 
def initializeWorld():
    os.system("cls||clear")
    print("------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")

def getPlayerName():
    playerName = input("Defina seu nome:\n")
    os.system("cls||clear")
    return playerName

def clearTerminal():
    input("Aperte Enter para continuar!")
    os.system("cls||clear")

def msgInitialWorld():
    print("Você precisa de Pokemãos para conquistar estádios, procure e capture-os!\n")
    clearTerminal()

def openMenu(playerName):
    print(f"Jogador {playerName} você acaba de abrir sua MAODEX.\nO que você deseja fazer agora?")
    print("\n1 - Visualizar Pokemaos\n2 - Duelas por ginásios\n3 - Capturar Pokemãos\n 4 - Sair")
    
def startHistory(Pokemao, Player, playerName, startPokemaos):
    print("Sua jornada começa agora!\nNote que você já começa com um Pokemão.")
    initialPokemaos = startPokemaos()
    pokemaoSorted = Pokemao.definitionPokemao(initialPokemaos)
    player = Player(playerName, pokemaoSorted)
    clearTerminal()
    print(f"Mestre Pokemao {player.name}, seu pokemão inicial é:" + f"{player.pokemaos[0].color[0]} {player.pokemaos[0].name} {TextColors.ENDC}")
    clearTerminal()
    openMenu(player.name)
