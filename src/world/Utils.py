import os


class TextColors:
    ENDC = '\033[0m'





def getNameOfPlayer():
    playerName = input("Defina seu nome:\n")
    os.system("cls||clear")
    return playerName



def infoInitialPokemons(clearTerminal):
    print("Você precisa de pokemãos, para isso é necessário capturá-los")
    print("Ao obter 3 pokemãos, você poderá disputar batalhas em prol de se tornar um líder pokemão")
    clearTerminal()


def initializeWorld():
    os.system("cls||clear")
    print(
        "------------ Seja bem-vindo ao mundo pokemão, se prepare pois você encontrará bastante aventura! ------------ \nBatalhe com bravura!\n")


def intialStoryWithFirstPokemon(playerName, initialPokemaos, Pokemao, Player, clearTerminal):
    print(
        "Agora você começará sua jornada no mundo pokemão.\nNote que você já começa com um pokemão e poderá capturar mais ao longo de sua jornada!")
    initialPokemao = initialPokemaos()
    pokemaoSorted = Pokemao.definitionPokemao(initialPokemao)

    player = Player(playerName, pokemaoSorted)
    clearTerminal()
    print(
        f"Mestre pokemão {player.name}, seu pokemão inicial é: " + f"{player.pokemaos[0].color} {player.pokemaos[0].name} {TextColors.ENDC}")
    clearTerminal()
    return player


