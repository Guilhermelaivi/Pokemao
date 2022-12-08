import os


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

def startHistory(Pokemao, Player, playerName, startPokemaos):
    print("Sua jornada começa agora!\nNote que você já começa com um Pokemão.")
    initialPokemao = startPokemaos()
    pokemaoSorted = Pokemao.definitionPokemao(initialPokemao)
    player = Player(playerName, initialPokemao)